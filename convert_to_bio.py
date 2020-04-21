import json
import nltk
import re
from nltk.tokenize.simple import SpaceTokenizer

tk = SpaceTokenizer()


def get_bio_target(opinion):
    try:
        text, idxs = opinion["Target"]
    # will throw exception if the opinion target is None type
    except TypeError:
        return []
    except ValueError:
        return []
    # get the beginning and ending indices
    if len(text) > 1:
        updates = []
        #
        for t, idx in zip(text, idxs):
            bidx, eidx = idx.split(":")
            bidx = int(bidx)
            eidx = int(eidx)
            polarity = opinion["Polarity"]
            target_tokens = t.split()
            label = "-targ-{0}".format(polarity)
            #
            tags = []
            for i, token in enumerate(target_tokens):
                if i == 0:
                    tags.append("B" + label)
                else:
                    tags.append("I" + label)
            updates.append((bidx, tags))
        return updates
    else:
        bidx, eidx = idxs[0].split(":")
        bidx = int(bidx)
        eidx = int(eidx)
        polarity = opinion["Polarity"]
        target_tokens = text[0].split()
        label = "-targ-{0}".format(polarity)
        #
        tags = []
        for i, token in enumerate(target_tokens):
            if i == 0:
                tags.append("B" + label)
            else:
                tags.append("I" + label)
        return [(bidx, tags)]

def get_bio_expression(opinion):
    try:
        text, idxs = opinion["Polar_expression"]
    # will throw exception if the opinion target is None type
    except TypeError:
        return []
    except ValueError:
        return []
    # get the beginning and ending indices
    if len(text) > 1:
        updates = []
        #
        for t, idx in zip(text, idxs):
            bidx, eidx = idx.split(":")
            bidx = int(bidx)
            eidx = int(eidx)
            polarity = opinion["Polarity"]
            target_tokens = t.split()
            label = "-exp-{0}".format(polarity)
            #
            tags = []
            for i, token in enumerate(target_tokens):
                if i == 0:
                    tags.append("B" + label)
                else:
                    tags.append("I" + label)
            updates.append((bidx, tags))
        return updates
    else:
        bidx, eidx = idxs[0].split(":")
        bidx = int(bidx)
        eidx = int(eidx)
        polarity = opinion["Polarity"]
        target_tokens = text[0].split()
        label = "-exp-{0}".format(polarity)
        #
        tags = []
        for i, token in enumerate(target_tokens):
            if i == 0:
                tags.append("B" + label)
            else:
                tags.append("I" + label)
        return [(bidx, tags)]

def get_bio_holder(opinion):
    try:
        text, idxs = opinion["Source"]
    # will throw exception if the opinion target is None type
    except TypeError:
        return []
    except ValueError:
        return []
    # get the beginning and ending indices
    if len(text) > 1:
        updates = []
        #
        for t, idx in zip(text, idxs):
            bidx, eidx = idx.split(":")
            bidx = int(bidx)
            eidx = int(eidx)
            target_tokens = t.split()
            label = "-holder"
            #
            tags = []
            for i, token in enumerate(target_tokens):
                if i == 0:
                    tags.append("B" + label)
                else:
                    tags.append("I" + label)
            updates.append((bidx, tags))
        return updates
    else:
        bidx, eidx = idxs[0].split(":")
        bidx = int(bidx)
        eidx = int(eidx)
        target_tokens = text[0].split()
        label = "-holder"
        #
        tags = []
        for i, token in enumerate(target_tokens):
            if i == 0:
                tags.append("B" + label)
            else:
                tags.append("I" + label)
        return [(bidx, tags)]


def replace_with_labels(labels, offsets, bidx, tags):
    # There are some annotations that missed token level (left out a leading character) that we need to fix
    try:
        token_idx = offsets.index(bidx)
        for i, tag in enumerate(tags):
            labels[i + token_idx] = tag
        return labels
    except:
        return labels


def create_bio_labels(text, opinions):
    offsets = [l[0] for l in tk.span_tokenize(text)]
    #
    labels = ["O"] * len(offsets)
    #
    anns = []

    # TODO: deal with targets which can have multiple polarities, due to
    # contrasting polar expressions
    for o in opinions:
        try:
            anns.extend(get_bio_holder(o))
            anns.extend(get_bio_target(o))
            anns.extend(get_bio_expression(o))
        except:
            pass
    #
    for bidx, tags in anns:
        labels = replace_with_labels(labels, offsets, bidx, tags)
    return labels


def to_bio(dataset):
    tokenized = []
    all_labels = []
    for i, sent in enumerate(dataset):
        #print(i)
        text = sent["text"]
        opinions = sent["opinions"]
        tokens = text.split()
        labels = create_bio_labels(text, opinions)
        tokenized.append(tokens)
        all_labels.append(labels)
    return tokenized, all_labels

if __name__ == "__main__":

    for split in ["train", "dev", "test"]:
        with open("data/{0}.json".format(split)) as o:
            dev = json.load(o)

        tokenized, labels = to_bio(dev)

        with open("data/{0}.conll".format(split), "w") as outfile:
            for meta, sent, label in zip(dev, tokenized, labels):
                sent_id = meta["sent_id"]
                outfile.write("# sent_id = {0}\n".format(sent_id))
                for token, tag in zip(sent, label):
                    outfile.write("{0}\t{1}\n".format(token, tag))
                outfile.write("\n")
