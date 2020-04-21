import re
import csv
import os
import argparse
import json


def get_anns(ann_file):
    """
    This function takes a curated BRAT annotation file as input
    and returns a dictionary of the annotation IDs to their labels (ann_dict)
    as well as a dictionary of full opinions (anns_out), where the keys are the event IDs from BRAT and the values are dictionaries of the opinion.
    """

    # First we extract the annotations from the tab separated BRAT file
    ann_dict = {}
    anns = csv.reader(open(ann_file), delimiter="\t")
    for ann in anns:
        ann_dict[ann[0]] = ann[1:]


    # Second, we iterate over the ann_dict to find the sentiment events:
    # (E or EFINP) and keep them in anns_out
    anns_out = {}
    for ann_idx, value in ann_dict.items():
        # for each sentiment event, get all triggers
        if "E" in ann_idx or "EFINP" in ann_idx:
            # set up subdict for this event
            anns_out[ann_idx] = {"Source": [], "Target": [], "Polar_expression": [], "Polarity": None, "Intensity": None, "NOT": False, "Source_is_author": False, "Target_is_general": False}


            triggers = value[0].split()

            # Triggers contains minimally ['Polar_expression:annotation_idx'],
            # but can also contain 'Target:annotation_idx' and
            # 'Source:annotation_idx'

            for trigger in triggers:
                # split each trigger into tag and idx, e.g. ('Target', 'T12')
                tag, trigger_idx = trigger.split(":")

                # get the trigger annotation from ann_dict, e.g. 'Entity 12 18'
                t_exp = ann_dict[trigger_idx][0]

                # keep only the character offsets
                _ , spans = t_exp.split(" ", maxsplit=1)

                # Since there can be discontinuous spans, we have to check
                # If there are discontinuous spans they are marked with a
                # semicolon, e.g. '10 14;20 27'
                if ";" in spans:
                    spans = spans.split(";")
                    for span in spans:
                        anns_out[ann_idx][tag].append(span)

                # If there are no discontinuous spans, add them directly to
                # the opinion dictionary
                else:
                    try:
                        anns_out[ann_idx][tag].append(spans)
                    except KeyError:
                        print(ann_file)
                        print("KeyError: '{0}'".format(tag))
                        break

    # Finally, we perform a second pass to get the attributes for the events
    for idx, value in ann_dict.items():
        if "A" in idx:
            try:
                # These are the Polarity and Intensity aspects, which have
                # both an annotation id to an event, and a label
                tag, ann_idx, label = value[0].split()
                anns_out[ann_idx][tag] = label
            except ValueError:
                # Here we handle Target_is_general, Not_on_topic (NOT),
                # Source_is_author, which are all boolean values and therefore
                # do not have a label
                tag, ann_idx = value[0].split()
                try:
                    anns_out[ann_idx][tag] = True
                # Currently, there are some Aspect annotations that have ann_idx which points to a target, rather than an event. So I chose to leave these out for the moment.
                except KeyError:
                    pass

    return ann_dict, anns_out

def convert_to_json(data_dir):
    """
    This function takes a directory with BRAT annotations for fine-grained sentiment and returns a json object which is a list of dictionaries. Each dictionary represents a sentence from the dataset.
    """
    data = []

    for file in os.listdir(data_dir):

        if ".txt" in file:
            textfile = os.path.join(data_dir, file)
            ann_file = textfile[:-4] + ".ann"
            doc_idx = os.path.basename(textfile)[:-4].split("_")[0]

            #print(textfile)

            # open text file
            text = open(textfile).read()

            # get all annotations such that we have spans associated with tags in a dictionary
            ann_dict, anns = get_anns(ann_file)

            paragraphs = text.split("\n\n")
            sents = [p.split("\n") for p in paragraphs]

            # get all of the character offsets for paragraphs
            paragraph_offsets = []
            i = 0
            for p in paragraphs:
                offset = (i, i + len(p))
                i += len(p) + 2
                paragraph_offsets.append(offset)

            # get all of the character offsets for sentences in each paragraph
            i = 0
            sent_offsets = []
            for p in sents:
                poff = []
                for j, sent in enumerate(p):
                    offset = (i, i + len(sent))
                    poff.append(offset)
                    if j == len(p) - 1:
                        i += len(sent)
                    else:
                        i += len(sent) + 1
                sent_offsets.append(poff)
                i += 2

            # sort opinions into their sentences
            opinions = {}

            for opinion_idx, opinion in anns.items():
                bidx, eidx = opinion["Polar_expression"][0].split()
                bidx = int(bidx)
                for i, p in enumerate(sent_offsets):
                    for j, (b, e) in enumerate(p):
                        if bidx >= b and bidx <= e:
                            sent_id = "{0}-{1}-{2}".format(doc_idx,
                                                           str(i + 1).zfill(2),
                                                           str(j + 1).zfill(2))
                            # Get the text and new offsets for source, target and polar expression

                            if len(opinion["Source"]) > 0:
                                raw_text = []
                                offsets = []
                                for s in opinion["Source"]:
                                    bidx, eidx = s.split()
                                    bidx = int(bidx)
                                    eidx = int(eidx)
                                    # get raw text
                                    raw = text[bidx:eidx]
                                    raw_text.append(raw)
                                    # update character offsets
                                    new_bidx = bidx - b
                                    new_eidx = eidx - b
                                    offset = "{0}:{1}".format(new_bidx,
                                                              new_eidx)
                                    offsets.append(offset)
                                opinion["Source"] = [raw_text, offsets]

                            if len(opinion["Target"]) > 0:
                                raw_text = []
                                offsets = []
                                for s in opinion["Target"]:
                                    bidx, eidx = s.split()
                                    bidx = int(bidx)
                                    eidx = int(eidx)
                                    # get raw text
                                    raw = text[bidx:eidx]
                                    raw_text.append(raw)
                                    # update character offsets
                                    new_bidx = bidx - b
                                    new_eidx = eidx - b
                                    offset = "{0}:{1}".format(new_bidx,
                                                              new_eidx)
                                    offsets.append(offset)
                                opinion["Target"] = [raw_text, offsets]

                            if len(opinion["Polar_expression"]) > 0:
                                raw_text = []
                                offsets = []
                                for s in opinion["Polar_expression"]:
                                    bidx, eidx = s.split()
                                    bidx = int(bidx)
                                    eidx = int(eidx)
                                    # get raw text
                                    raw = text[bidx:eidx]
                                    raw_text.append(raw)
                                    # update character offsets
                                    new_bidx = bidx - b
                                    new_eidx = eidx - b
                                    offset = "{0}:{1}".format(new_bidx,
                                                              new_eidx)
                                    offsets.append(offset)
                                opinion["Polar_expression"] = [raw_text, offsets]




                            if sent_id in opinions:
                                opinions[sent_id].append(opinion)
                            else:
                                opinions[sent_id] = [opinion]


            # Create sent_jsons
            for i, p in enumerate(sent_offsets):
                for j, s in enumerate(p):

                    # set up json
                    sent_json = {"sent_id": None, "text": "", "opinions": []}

                    # Create sent_id
                    sent_id = "{0}-{1}-{2}".format(doc_idx,
                                                   str(i + 1).zfill(2),
                                                   str(j + 1).zfill(2))
                    sent_json["sent_id"] = sent_id

                    # get raw text
                    bidx, eidx = sent_offsets[i][j]
                    raw_text = text[bidx:eidx]
                    sent_json["text"] = raw_text

                    # include opinions (updating offsets)
                    try:
                        sent_json["opinions"] = opinions[sent_id]
                    except KeyError:
                        pass

                    # add to overall data_json
                    data.append(sent_json)

    return data

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_dir", default="data", help="location of directory with train, dev, test subdirectories.")

    args = parser.parse_args()

    for split in ["train", "dev", "test"]:

        data = convert_to_json(os.path.join(args.data_dir, split))

        with open(os.path.join(args.data_dir, split + ".json"), "w") as out:
            json.dump(data, out)
