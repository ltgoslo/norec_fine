import os
from nltk import FreqDist
from nltk.corpus import stopwords
import re
import numpy as np
import matplotlib.pyplot as plt
import argparse
import json


def add_to_dist(polarity, intensity):
    x = np.zeros(6)
    if polarity == "Negative":
        if intensity == "Strong":
            x[0] = 1
        elif intensity == "Standard":
            x[1] = 1
        elif intensity == "Slight":
            x[2] = 1
    elif polarity == "Positive":
        if intensity == "Slight":
            x[3] = 1
        elif intensity == "Standard":
            x[4] = 1
        elif intensity == "Strong":
            x[5] = 1
    return x


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--normalize", action="store_true")
    parser.add_argument("--plot", action="store_true")

    args = parser.parse_args()

    num_sents = {"train": 0, "dev": 0, "test": 0}
    num_subjective_sents = {"train": 0, "dev": 0, "test": 0}
    sent_lengths = {"train": [], "dev": [], "test": []}

    num_targets = {"train": 0, "dev": 0, "test": 0}
    num_unique_targets = {"train": 0, "dev": 0, "test": 0}
    targ_lengths = {"train": [], "dev": [], "test": []}

    num_source = {"train": 0, "dev": 0, "test": 0}
    num_unique_source = {"train": 0, "dev": 0, "test": 0}
    source_lengths = {"train": [], "dev": [], "test": []}

    num_polar_exp = {"train": 0, "dev": 0, "test": 0}
    num_unique_polar_exp = {"train": 0, "dev": 0, "test": 0}
    polar_exp_lengths = {"train": [], "dev": [], "test": []}

    implicit_targets = {"train": 0, "dev": 0, "test": 0}
    implicit_holders = {"train": 0, "dev": 0, "test": 0}

    discontinuous_polar_exp = {"train": 0, "dev": 0, "test": 0}
    discontinuous_target = {"train": 0, "dev": 0, "test": 0}
    discontinuous_holder = {"train": 0, "dev": 0, "test": 0}

    not_on_topic = {"train": 0, "dev": 0, "test": 0}

    polarity_distribution = {"train": np.zeros(6),
                             "dev": np.zeros(6),
                             "test": np.zeros(6)
                             }

    num_subjective_sents_with_multiple_polarities = {"train": 0, "dev": 0, "test": 0}

    for split in ["train", "dev", "test"]:
        with open(split + ".json") as infile:
            data = json.load(infile)
        for sentence in data:
                num_sents[split] += 1
                sources = []
                targets = []
                expressions = []
                polarities = []
                sent_lengths[split].append(len(sentence["text"].split()))
                if len(sentence["opinions"]) > 0:
                    num_subjective_sents[split] += 1
                for opinion in sentence["opinions"]:
                    NOT = opinion["NOT"]
                    if NOT is True:
                        not_on_topic[split] += 1
                    source = opinion["Source"][0]
                    # continue only if there actually is a source
                    if source != []:
                        num_source[split] += 1
                        sources.append(" ".join(source))
                        if len(source) > 1:
                            discontinuous_holder[split] += 1
                        source_len = 0
                        for text in source:
                            source_len += len(text.split())
                        source_lengths[split].append(source_len)
                    else:
                        implicit_holders[split] += 1
                    # continue only if there actually is a target
                    target = opinion["Target"][0]
                    if target != []:
                        num_targets[split] += 1
                        targets.append(" ".join(target))
                        if len(target) > 1:
                            discontinuous_target[split] += 1
                        target_len = 0
                        for text in target:
                            target_len += len(text.split())
                        targ_lengths[split].append(target_len)
                    else:
                        implicit_targets[split] += 1
                    # get opinion expressions
                    exp = opinion["Polar_expression"][0]
                    num_polar_exp[split] += 1
                    expressions.append(" ".join(exp))
                    if len(exp) > 1:
                        discontinuous_polar_exp[split] += 1
                    exp_len = 0
                    for text in exp:
                        exp_len += len(text.split())
                    polar_exp_lengths[split].append(exp_len)
                    #
                    pol = opinion["Polarity"]
                    polarities.append(pol)
                    intensity = opinion["Intensity"]
                    polarity_distribution[split] += add_to_dist(pol, intensity)

                num_unique_source[split] += len(set(sources))
                num_unique_targets[split] += len(set(targets))
                num_unique_polar_exp[split] += len(set(expressions))
                if len(set(polarities)) > 1:
                    num_subjective_sents_with_multiple_polarities[split] += 1

    for split in ["train", "dev", "test"]:
        print("{} ############################################".format(split))
        print("Sents: {0}".format(num_sents[split]))
        print("---- subjective: {0}".format(num_subjective_sents[split]))
        print("---- with multiple polarities: {0}".format(num_subjective_sents_with_multiple_polarities[split]))
        print("---- min len: {0}".format(np.min(sent_lengths[split])))
        print("---- max len: {0}".format(np.max(sent_lengths[split])))
        print("---- ave len: {0:.1f}".format(np.mean(sent_lengths[split])))
        print()
        print("Holders: {0}".format(num_source[split]))
        print("---- unique: {0}".format(num_unique_source[split]))
        print("---- min len: {0}".format(np.min(source_lengths[split])))
        print("---- max len: {0}".format(np.max(source_lengths[split])))
        print("---- ave len: {0:.1f}".format(np.mean(source_lengths[split])))
        print("---- implicit: {0}".format(implicit_holders[split]))
        print("---- discontinuous: {0}".format(discontinuous_holder[split]))
        print("---- ave num per subj sent: {0:.1f}".format(num_unique_source[split] / num_subjective_sents[split]))
        print()
        print("Targets: {0}".format(num_targets[split]))
        print("---- unique: {0}".format(num_unique_targets[split]))
        print("---- min len: {0}".format(np.min(targ_lengths[split])))
        print("---- max len: {0}".format(np.max(targ_lengths[split])))
        print("---- ave len: {0:.1f}".format(np.mean(targ_lengths[split])))
        print("---- implicit: {0}".format(implicit_targets[split]))
        print("---- discontinuous: {0}".format(discontinuous_target[split]))
        print("---- ave num per subj sent: {0:.1f}".format(num_unique_targets[split] / num_subjective_sents[split]))
        print("---- Not on Topic: {0}".format(not_on_topic[split]))
        print()
        print("Polar Exps.: {0}".format(num_polar_exp[split]))
        print("---- unique: {0}".format(num_unique_polar_exp[split]))
        print("---- min len: {0}".format(np.min(polar_exp_lengths[split])))
        print("---- max len: {0}".format(np.max(polar_exp_lengths[split])))
        print("---- ave len: {0:.1f}".format(np.mean(polar_exp_lengths[split])))
        print("---- discontinuous: {0}".format(discontinuous_polar_exp[split]))
        print("---- ave num per subj sent: {0:.1f}".format(num_unique_polar_exp[split] / num_subjective_sents[split]))
        print()
        print("Polarity distribution - Strong Neg ----> Strong Pos")
        dist = polarity_distribution[split] / polarity_distribution[split].sum()
        print("{0:.3f}\t{1:.3f}\t{2:.3f}\t{3:.3f}\t{4:.3f}\t{5:.3f}\t".format(*dist))
        print()


    print("Total###########################")
    print("Sents: {0}".format(sum(num_sents.values())))
    print("---- subjective: {0}".format(sum(num_subjective_sents.values())))
    print("---- with multiple polarities: {0}".format(sum(num_subjective_sents_with_multiple_polarities.values())))
    all_sent_lengths = [i for k in sent_lengths.values() for i in k]
    print("---- min len: {0}".format(np.min(all_sent_lengths)))
    print("---- max len: {0}".format(np.max(all_sent_lengths)))
    print("---- ave len: {0:.1f}".format(np.mean(all_sent_lengths)))
    print()
    print("Holders: {0}".format(sum(num_source.values())))
    print("---- unique: {0}".format(sum(num_unique_source.values())))
    all_source_lengths = [i for k in source_lengths.values() for i in k]
    print("---- min len: {0}".format(np.min(all_source_lengths)))
    print("---- max len: {0}".format(np.max(all_source_lengths)))
    print("---- ave len: {0:.1f}".format(np.mean(all_source_lengths)))
    print("---- discontinuous: {0}".format(sum(discontinuous_holder.values())))
    print("---- ave num per subj sent: {0:.1f}".format(sum(num_unique_source.values()) / sum(num_subjective_sents.values())))
    print()
    print("Targets: {0}".format(sum(num_targets.values())))
    print("---- unique: {0}".format(sum(num_unique_targets.values())))
    all_targ_lengths = [i for k in targ_lengths.values() for i in k]
    print("---- min len: {0}".format(np.min(all_targ_lengths)))
    print("---- max len: {0}".format(np.max(all_targ_lengths)))
    print("---- ave len: {0:.1f}".format(np.mean(all_targ_lengths)))
    print("---- discontinuous: {0}".format(np.sum(list(discontinuous_target.values()))))
    print("---- ave num per subj sent: {0:.1f}".format(sum(num_unique_targets.values()) / sum(num_subjective_sents.values())))
    print("---- Not on Topic: {0}".format(np.sum(list(not_on_topic.values()))))
    print()
    print("Polar Exps.: {0}".format(sum(num_polar_exp.values())))
    print("---- unique: {0}".format(sum(num_unique_polar_exp.values())))
    all_exp_lengths = [i for k in polar_exp_lengths.values() for i in k]
    print("---- min len: {0}".format(np.min(all_exp_lengths)))
    print("---- max len: {0}".format(np.max(all_exp_lengths)))
    print("---- ave len: {0:.1f}".format(np.mean(all_exp_lengths)))
    print("---- discontinuous: {0}".format(np.sum(list(discontinuous_polar_exp.values()))))
    print("---- ave num per subj sent: {0:.1f}".format(sum(num_unique_polar_exp.values()) / sum(num_subjective_sents.values())))
    print()
    print("Polarity distribution - Strong Neg ----> Strong Pos")
    full_polarity_distribution = polarity_distribution["train"] + polarity_distribution["dev"] + polarity_distribution["test"]
    full_polarity_distribution /= full_polarity_distribution.sum()
    print("{0:.3f}\t{1:.3f}\t{2:.3f}\t{3:.3f}\t{4:.3f}\t{5:.3f}\t".format(*full_polarity_distribution))
    print()

    if args.plot:

        full_polarity_distribution = polarity_distribution["train"] + polarity_distribution["dev"] + polarity_distribution["test"]
        if args.normalize:
            full_polarity_distribution /= full_polarity_distribution.sum()

        fig, ax = plt.subplots(figsize=(3, 3))
        ax.spines["top"].set_visible(False)
        ax.spines["left"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["bottom"].set_visible(False)
        ax.tick_params(axis=u'both', which=u'both',length=0)

        ax.barh(range(len(full_polarity_distribution)), full_polarity_distribution, zorder=3)
        ax.set_yticklabels(["", "strong neg.", "neg.", "slight neg.", "slight pos.", "pos.", "strong pos."])


        plt.grid(axis="x", linestyle="--", zorder=0)
        plt.tight_layout()
        plt.show()
