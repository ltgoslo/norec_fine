# NoReC_fine

This dataset is described in the paper _A Fine-Grained Sentiment Dataset for Norwegian_ by L. Øvrelid, P. Mæhlum, J. Barnes, and E. Velldal, accepted for LREC 2020, [see arXiv preprint here](https://arxiv.org/abs/1911.12722).

## Overview
While the previously released dataset [NoReC_eval](https://github.com/ltgoslo/norec_eval) labeled sentences as to whether they are _evaluative_ or sentiment-bearing, NoReC_fine expands on these annotations by also labeling polar expressions, holders and targets. The data comprises roughly 8000 sentences across almost 300 reviews and 10 different thematic categories (literature, products, restaurants, etc.), and is a subset of the [Norwegian Review Corpus](https://github.com/ltgoslo/norec) (NoReC; [Velldal et al. 2018](http://www.lrec-conf.org/proceedings/lrec2018/pdf/851.pdf)).

## Conversion from BRAT to Json

We include a script to convert from BRAT format to a Json format that is easier to deal with. To get the converted data, simply run:

```
python3 convert_to_json.py
```

You will then have train.json, dev.json, and test.json in the data directory.

You can import them by using the json library in python:

```
>>> import json
>>> data = {}
>>> for name in ["train", "dev", "test"]:
        with open("data/{0}.json".format(name)) as infile:
            data[name] = json.load(infile)
```


## Json Format

Each sentence has a dictionary with the following keys and values:
---
"sent_id": unique NoReC identifier for document + paragraph + sentence which lines up with the identifiers from the document and sentence-level NoReC data

"text": raw text

"opinions": list of all opinions (dictionaries) in the sentence

Additionally, each opinion in a sentence is a dictionary with the following keys and values:
---
"Source": a list of text and character offsets for the opinion holder

"Target": a list of text and character offsets for the opinion target

"Polar_expression": a list of text and character offsets for the opinion expression

"Polarity": sentiment label ("Negative", "Positive")

"Intensity": sentiment intensity ("Standard", "Strong", "Slight")

"NOT": Whether the target is 'Not on Topic' (True, False)

"Target_is_general": (True, False)

"NFP": Whether or not the Source is 'Not First Person' (True, False)

"Type": Whether the polar expression is Evaluative (E) or Evaluative Fact Implied (EFINP)

```
{
    'sent_id': '202263-20-01',

    'text': 'Touchbetjeningen brukes også til å besvare innkomne mobilanrop , og Sennheiser skryter av å ha doble mikrofoner i øreklokkene for å kutte ned på støyen .',

    'opinions': [

                    {
                     'Source': [['Sennheiser'], ['68:78']],

                     'Target': [['øreklokkene'], ['114:125']],

                     'Polar_expression': [['skryter av å ha doble mikrofoner i øreklokkene for å kutte ned på støyen'], ['79:151']],

                     'Polarity': 'Positive',

                     'Intensity': 'Standard',

                     'NOT': False,

                     'Source_is_author': False,

                     'Target_is_general': True,

                     'NFP': True,

                     'Type': 'E'
                     }

                 ]
}


```

Note that for a single text, it is common to have many opinions. At the same time, it is common for many datasets to lack one of the elements of an opinion, e.g. the holder. In this case, the value for that element is None.

