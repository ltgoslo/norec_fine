import json
from nltk.tokenize.simple import SpaceTokenizer

tk = SpaceTokenizer()

def check_offsets(sent):
    #
    sent_boffsets = [l[0] for l in tk.span_tokenize(sent["text"])]
    sent_eoffsets = [l[1] for l in tk.span_tokenize(sent["text"])]
    #
    for opinion in sent["opinions"]:
        source = opinion["Source"]
        if len(source[0]):
            for offsets in source[1]:
                boff = int(offsets.split(":")[0])
                eoff = int(offsets.split(":")[1])
                if boff not in sent_boffsets:
                    print("{0} : {1} : {2}".format(sent["sent_id"], boff, " ".join(source[0])))
                if eoff not in sent_eoffsets:
                    print("{0} : {1} : {2}".format(sent["sent_id"], eoff, " ".join(source[0])))
        #
        target = opinion["Target"]
        if len(target[0]):
            for offsets in target[1]:
                boff = int(offsets.split(":")[0])
                eoff = int(offsets.split(":")[1])
                if boff not in sent_boffsets:
                    print("{0} : {1} : {2}".format(sent["sent_id"], boff, " ".join(target[0])))
                if eoff not in sent_eoffsets:
                    print("{0} : {1} : {2}".format(sent["sent_id"], eoff, " ".join(target[0])))
        #
        exp = opinion["Polar_expression"]
        if len(exp[0]):
            for offsets in exp[1]:
                boff = int(offsets.split(":")[0])
                eoff = int(offsets.split(":")[1])
                if boff not in sent_boffsets:
                    print("{0} : {1} : {2}".format(sent["sent_id"], boff, " ".join(exp[0])))
                if eoff not in sent_eoffsets:
                    print("{0} : {1} : {2}".format(sent["sent_id"], eoff, " ".join(exp[0])))

def check_target_NOT_consistency(sent):
    targets = {}
    for opinion in sent["opinions"]:
        target = " ".join(opinion["Target"][0])
        if target not in targets:
            targets[target] = []
            targets[target].append(opinion["NOT"])
        else:
            targets[target].append(opinion["NOT"])
    for target, nots in targets.items():
        if len(set(nots)) > 1:
            print("{0} : {1}: Conflicting NOT annotations".format(sent["sent_id"], target))

# ADD check target is general consistency
def check_target_is_general_consistency(sent):
    targets = {}
    for opinion in sent["opinions"]:
        target = " ".join(opinion["Target"][0])
        if target not in targets:
            targets[target] = []
            targets[target].append(opinion["Target_is_general"])
        else:
            targets[target].append(opinion["Target_is_general"])
    for target, attributes in targets.items():
        if len(set(attributes)) > 1:
            print("{0} : {1}: Conflicting Target_is_general annotations".format(sent["sent_id"], target))

# Source is author /
def check_source_is_author_consistency(sent):
    for opinion in sent["opinions"]:
        nfp = None
        source_is_author = None
        try:
            nfp = opinion["Not_First_Person"]
        except KeyError:
            pass
        try:
            source_is_author = opinion["Source_is_author"]
        except KeyError:
            pass
        # Not_First_Person and Source_is_author should not be the same
        # and there should be at least one annotated, i.e. not (NONE, NONE)
        if len(set([nfp, source_is_author]))!= 2:
            print("{0} : {1}: Conflicting NFP and Source_is_author annotations".format(sent["sent_id"], " ".join(opinion["Polar_expression"])))


if __name__ == "__main__":

    for split in ["train", "dev", "test"]:
        with open("En_liten_sjekk/{0}.json".format(split)) as o:
            data = json.load(o)

            print()
            print(split)
            print()
            for sent in data:
                check_offsets(sent)
                check_target_NOT_consistency(sent)
                check_target_is_general_consistency(sent)
                check_source_is_author_consistency(sent)
