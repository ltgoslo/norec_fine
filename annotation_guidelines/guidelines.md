# Annotation guidelines for SANT, Fine-grained
April 2019

# Table of Contents

1. [Introduction](#introduction)
2. [Part 1: Terminology](#part-1-terminology)\
2.1 [Terms](#terms)\
2.2 [Polar Expression](#polar-expression)\
2.3 [Target](#target)\
2.4 [Source](#source)\
2.5 [Type](#type)
3. [Part 2: Brat](#part-2-brat)\
3.1 [Brat](#brat)\
3.2 [Entities, Events and Attributes](#entities-events-and-attributes)

## Introduction
These guidelines are intended to give an introduction to fine grained annotation for the SANT project, based on the previous sentence level annotations. The sentences that were labeled as evaluative in the previous round are annotated on a more fine-grained level, based largely upon the schema introduced in Van de Kauter et al. (link). These guidelines come in three parts: an introduction to terminology, an introduction to Brat labels and terminology, and a detailed description of how to annotate and how to delimit spans.

# Part 1: Terminology

## Terms
The following paragraphs attempt to describe some of the terms commonly used in more fine-grained analyses, that are not used much in sentence or document level annotation schemes. These guidelines only cover the terms relevant for the current annotation scheme. Other authors might use other, more elaborate schemes.

### Polar expression
A polar expression is the part of a sentence that contributes to the evaluative and polar power of the sentence. For some sentences that might mean just a sentiment lexeme such as "to love", "awful" or "winner". These expression might also include modifiers, including intesifiers such as "very" or modal elements such as "should". Sometimes larger, more complex expressions constitute the polar expression. This will be discussed further at a later point in these guidelines.

### Target
The target is the entity that the sentiment is expressed towards\[Van de kauter, guidelines, chap3\]. In the sentence "I like this car", the target of the polar expression "like" is "car". Targets are not always easy to identify, as they are often nested, and reprent increasingly detailed aspects of the object being reviewed. We will focus on the canonical aspects in a review, see chapter 3.

### Source
The source, or holder, is the one whose inner state <!--- citation ---> is reflected in the evaluation of the sentence. It is the one who _holds_ the evaluation. The source can be explicit or implicit, and it can belong to the author, or to someone else. All sentences that contained only evaluations that belonged to someone other than the author, was marked as NFP in the sentence level annotation. 

### Type
A sentence can contain several different polar expressions. Even though each sentence was marked in the previous annotation mark, it is still possible that there are different types of polar expressions in the same sentence. In order to capture the types of expressions present, the labels from the previous round are carried into this round. This means that the labels evaluative (E), evaluative fact-implied non-personal (EFINP), not on topic (NOT) and not first person (NFP) are carried over. Therefore, it is necessary to reevaluate each polar expression according to the sentence level guidelines. 


### Modifiers
Modifiers are expressions (words, phrases) that in some way alter the polarity or strength of a polar expression. We do not mark modifiers explicitly in this fine-grained annotation round, but it can be useful to be aware of which words might be modifiers, as they should always be part of the span of the polar expression they modify.


# Part 2: Brat

## Brat
In contrast to the sentence level annotations, the fine-grained annotations will be done in the free annotatotion tool Brat. Brat's interface is slightly different, but there are also some new functionalities. All these things are described on their [webpage](http://brat.nlplab.org/). The following are brief introductions to the various labels used for fine-grained annotation.

### Entities, Events and Attributes
Sources and targets are annotated as entities, while polar expressions are annotated as events. These events can optionally have relations to the source and target that belong to the expression, if they are present. An absence of these relations implies implicit relations. 

### Marking spans
Double clicking on a word marks it. The annotator can also hold down ctr, double clicking on a word, and then releasing ctrl, press shift at the place you want the span to go to. Spaces are ignored, so they can be marked without affecting the annotation.

### Discontinous spans
Discontinous spans can be marked in Brat by selecting "Add frag.(ment)" from the annotation window. In order to get this option, a span and an annotation (Entity, Polar expression) must be selected. After this, the option to add fragments will show up when the annotation is clicked.

### Multiple targets
When adding multiple targets to the same polar expression, which is something that can happen quite often, Brat will display an error message saying that two targets for the same polar expression is not allowed. In this case, mark the polar expression and chose the option "split", then select "target" and press OK. Brat will then split the polar expression into several identical polar expressions, one for each target.

### Comments (notes)
If you notice something interesting, or want to note a particular problem, then this can be noted in the "Notes"-section of the Brat annotation window. These comments will be saved as comments, and can be searched through at a later point. They will not be part of the visual representation of the annotations. We especially recommend commenting the following things: negation, sarcasm, irony, comparative.  

### Multiple expressions
As mentioned earlier, a sentence could have had several polar expressiones when annotated at sentence level. If this is the case, then each polar expression is marked separately, with each having their own targets and sources. Note, however, that there is a difference between having multiple sentiment lexemes and having multiple polar expressions. A polar expression can be complex, consisting of several sentiment lexemes, while not really being more than one polar expression.

### Known issues
There seems to be a problem with trying to create a discontinous span from a polar event that is overlapping with another polar event. Trying to add a fragment to one of them will result in both being extended, as seen in the following example. This can be circumvented by trying to start the polar event on the non-overlapping part, and then adding the overlapping part as a fragment.

A discontinous target cannot cross another target that is not part of itself. In these cases care should be taken to either simplify the structure or expand the span of one of the targets. 

### Curation
Curation is done by comparing the annotated document of two annotators. These annotations are put in a special format, where the annotations of both annotators are displayed together. The curator should then chose the annotation that most strictly adheres to the rules presented in the guidelines. The curation document is generated so that all sentences that are identically annotated among the two initial annotators are pre-tagged. This is to save the curator some work.


# Part 3: Annotation details
The following will be a discussion of the finer parts of the analysis.

### Entities
Entities are either sources or targets of a sentiment expression. Sources should, and tend to, be short, while targets can some times be longer.




#### Sources
Sources are not always explicitly mentioned, in fact, that seldomly seems to be the case. If they are, they can take many forms. Frequently it is in the form of pronouns, but they can also be expressed as nouns such as "(the) author", names, etc. A source is at first just marked as an entity. Then the source is marked as a relation between the polar expression event and a target. If the author is implicit but it is understood as being the author of the article, the event is given the attribute "source is author". If the author is implicit, but *not* the author of the article, then it is simply left out.  


[image1]: https://github.uio.no/SANT/fine-grained/blob/master/setning2.png "Labels"

![alt text][image1]
<br/>*Example 1: implicit source*
  
If the source is explicit, and the source is the author of the article, it is commonly indicates through the use of first person pronouns. Note that both *jeg* 'I' and *vi* 'we' are commonly used to refer to the author alone. Vi can refer to the editors or the organization evaluating the object. 

[image7]: https://github.uio.no/SANT/fine-grained/blob/master/images/source_example.png "Labels"

![alt text][image7]
<br/>*Example 2: explicit source*

In some cases the author writes about themselves in the third person.

It is also possible for the source to be expressed through a possessive pronoun followed by a noun phrase or something similar. In these cases, only the possessive pronoun is labeled.

[image8]: https://github.uio.no/SANT/fine-grained/blob/master/images/source_possessive.png "Labels"

![alt text][image8]
<br/>*Example 3: possessive pronoun source*

Several sentences are marked as Not first person (NFP) in the sentence level annotation. These sentences tend to have an explicit author (this is one of the reasons why we can label them as NFP), but note that given a specific context, these sentences too can have implicit authors. If a polar expression event has a source other than the author, it should be marked as NFP, as in the sentence level annotations.

#### Targets
Targets are what the polar expressions are about, and they are one of the main focuses of the annotation efforts. Targets are more often mentioned explicitly than sources, and there can be several of them in the same sentence. Target spans can be short, but should not be reduced if this means that information is lost. This means that information that does not aid in delimiting the target should not be included, while everything that is necessary in order to understand the full meaning of the target, should be included. Targets are only selected if they are canonical, meaning that they represent some common feature of the object being reviewed. 

[image9]: https://github.uio.no/SANT/fine-grained/blob/master/images/target_polar.png "Labels"

![alt text][image9]
<br/>*Example 4: explicit target *

It is not always easy to identify targets. Reviewed objects might have easily identifiable physical aspects, like how a tablet has a screen and memory. However, they can also be more abstract parts, such as price or ease of use. A target can also be an aspect of another aspect: a screen has a resolution, color quality, etc. We can imagine an aspect tree, spanning both upwards and downwards from the object being reviewed.

Targets are typically nouns, but in theory they can also be expressed through adjectives or verbs, as in "This computer is cheap". The target of "cheap" is the price of the computer, not the computer itself. In this case, however, we mark "This computer" as the target of the polar expression "cheap". As a rule, only the most general aspect is labeled in our annotation scheme, and only *canonical* aspects are marked as aspects at all. This means that only the most typical aspects of the object should be marked. All others should be seen as part of the polar expression.

#### Target-related polar expression attribute "Target is general"
The attribute target is general is meant to be used when the polar expression is about the thing being reviewed in the most general sence. This might happen on two different occations: When the polar expression is used in a general sence and the target is implicit, or when the object being reviewed is being referred to explicitly in the text, and that target is modified by a polar expression. "Target is general" is not used when a polar expression has a target that is at a lower ontological level than the object being reviewed. In this case, it is s

#### Words that combine the target with polar expressions
In addition to the above mentioned words like cheap, there are several cases where target and polar expression coincide. As Norwegian easily allow adective + noun compounds, these types of expressions might be encountered frequently. Some examples are compounds with "favoritt-", as in *favoritt-hodetelefoner* 'favourite headphones' (202263). Since sub-word tokens cannot be marked, these words should be marked as polar expressions.

#### Polar-target combinations as targets
In a few cases, it might happen that we encounter targets that are modified in a way that is both delimiting and polar. In these cases we would like to treat the combined polar expression plus target as one target, but brat does not allow for targets within targets. In this cases there are two options: ignore the nesting and treat the whole expression as a target, like we would have done had the modifying expression not been polar, or we can treat the delimiting polar expression as a separate polar expression.
If the polar expression is in fact delimiting, then it should be taken as part of the target. That is to say, if the reference of the target changes depending on whether the polar expression is included or not, then it should be included and treated as part of the polar expression. If, however, the polar expression is not really delimiting, but simply a description of the polar expression, then it should be treated as a separate polar expression. Note that in some cases, this polar expression might have other attributes than the polar expression after the target, as in the example below.

(example 1)
Den kjølige tonen er vakker.
Here, we do not want to say that all "tones" in the series are beautiful, this might overgeneralize the polar expression. Therefore, we want to include "kjølig" with the target. More generally, we usually want to include graduable adjectives with the thing they modify, as their polarity is rarely clear in isolation.



(example 2)
"Det hele gir en slags dårlig coverband-vibb , og den lekre kominasjonen av UK garage , grime og klubbmusikk som er å finne på den ambisiøse debutskiva Disc-Overy , drukner i en haltende framføring"


Here, the word "lekre" does not necessarily delimit "kombinasjonen av UK garage, grime og klubbmusikk". There is no other combination that we need to treat differently, and therefore we can treat "lekre" as a separate polar expression. Note, however, that "lekre" is not on topic, as it is not a positive comment on the current stage, but on the same target in a different setting, while the fact that this (otherwise positive) combination drowns, is negative for the object of the review.


#### Infinitive clauses as targets
One source of longer-than-usual targets is the infinitive clause.

In the following sentence, the whole infinitive clause is necessary to fully capture the polarity and evaluation of the sentence.

[image2]: https://github.uio.no/SANT/fine-grained/blob/master/setning1.png "Labels"

![alt text][image2]
<br/>*Example 5: infinitive clause target*

### Polar expressions
Polar expressions can take many forms. They are often adjectives, but verbs and nouns as polar expressions are not infrequent.
The span of a polar expression should be large enough to capture all necessary information, without including information. In order to judge what is relevant, think about whether the strength and polarity of the expression changes when considering the span.

In cases where a polar expression and a target together form a new polar expression, this entire pair is again labeled as a polar expression. This happens in comparative sentences, and in cases where targets at different levels all appear in the same sentence, or when polar expressions describe non-canonical aspects. 

#### Polar-like expressions in symopses
Some genres, like litterature and screen, often contain synopses as part of their reviews. In these synopses, seemingly polar words tend to be used to describe certain personality traits, or certain aspects of the movie. These words, however, do not reflect anyone's inner state, and should rather be seen as ways of describing these aspects.

"Colin Farrell spiller rollen som Peter , en foreldreløs tyv med et stort hjerte og en enda større skjebne"()

In this sentence, it might seem like "stort hjerte" indicates a positive evaluation of "Peter", but this should be seen as a way of describing the character's personality, and not a reflection of the author's inner state.



#### Punctuation marks
Certain punctuation marks, such as the exclamation mark (!) and the question mark (?) can be used to modify the evaluative force of an expression, and are therefore included in the polar expression if this is the case. Other punctuation marks, such as the colon, comma and period, do usually not contribute to the semantics of polar expressions, and are therefore not included. Should any other punctuation mark be used in a way that contributes to the semantics of the polar expression in that sentence, then it can be included. 

#### Demonstratives and articles
Demonstratives and articles are not included unless they come between a semantically important verb and whatever arguments it has. This is to avoid unecessary discontious spans. Quantifiers such as *noen* 'some' , *mange* 'many' and *litt* 'some' are always included if they are part of the polar expression. 

#### Verbs
Verbs are only included if they contribute to the semantics of the polar expression. If the tense of the verb has an impact on the meaning, then the verb is included even if the verb itself does not contribute much to the meaning. Note that if an entire review is written in the past tense, then past tense in that case will not be a contributing factor, but the past of the past would be. Verbs like "å være" (to be) and "å ha" (to have) are commonly used. Note that while "å bli" and "å få" are similar, they include a notion of change. We do not mark causativity in this annotation scheme, so when "å gjøre" is used causatively, it is not marked. 

\[...\] Virkemidlene _gjør_ at jeg ler høyt på steder hvor jeg tror serieskaperne ønsker at jeg egentlig skal bli revet med. \[...\]

#### Particle verbs and reflexive verbs
If a preposition in front of a target is part of a particle verb,  then it contributes to the semantics of the verb and should be included. If it is not, then it is not included in the polar expression or the target.

Reflexive verbs should always be annotated together with the reflexive pronoun.

##### Verbs expressing sentiment
Several verbs have only the function of expressing sentiment. These verbs include "synes" and "mene". These verbs are not annotated. Another set of verbs tend to report objective sense experiences, such as  *høre* 'hear', *føle* 'feel', *kjenne* 'feel', and are not necessarily polar in nature, but the s-forms of these verbs on the other hand tend to indicate personal evaluation. They are, however, not annotated, as they work similarly to *synes* and *mene*, in that they indicate evaluation, but not polarity. 
 
 <!--- mangler bedre navn, det er ikke resiprok, ikke passiv,-->
 
 #### Sentence level adverbs
Certain expressions such as “heldigvis”, “dessverre” work on a higher level, and might add evaluation and/or polarity to otherwise non-evaluative sentence. At this annotation level they are annotated together with the polar expression.

#### Words expressing sensatory input
Sensory information should be included as part of the polar expression. Often one might find expressions such as *flott å se på* 'great to look at' as in the example below. In these cases, we see this as a way of giving information about the way something is perceived, and this information can be useful. Technically, this indicates an aspect (appearance, texture, melody, etc.) of the target, but these aspects fall outside of the scope of targets in this annotation scheme, and these expressions are therefore included in the polar expression.

"Filmen står lenge på stedet hvil og blir aldri en thriller som coveret lover , selv om den altså er flott å se på"

#### Conjunctions and subjunctions
Conjunct expressions should as a general rule be treated as two expressions. In order to avoid multiple (unecessary) discontinous spans, conjunct expressions that share an element, should be seen as one. If the conjunct expression is a fixed expression, or otherwise not truly conjunct, then the whole expression should be marked as one. 

Subjunctions should not be included unless excluding them alone leads to a discontinous span.

[image6]: https://github.uio.no/SANT/fine-grained/blob/master/setning6.png "Labels"

![alt text][image6]



[image5]: https://github.uio.no/SANT/fine-grained/blob/master/setning5.png "Labels"

![alt text][image5]

#### Expletive subjects
Expletive subjects are generally not included in the span of polar expressions.

[image4]: https://github.uio.no/SANT/fine-grained/blob/master/setning4.png "Labels"

![alt text][image4]


### Polarity
When annotating relations between polar expressions and their targets, the relation can be of two polarities: positive and negative. When annotating these at this level, consider the polarity of the expression _in combination with_ its target. This is because targets (and also sources) together form the context in which we interpret the polar expression, and therefore they can play a part in what determines the polarity. A polar expression alone can have various interpretations depending on what the target is. For E sentences we usually have a clear sentiment expression, and your task is then to identify whether it is positive or negative. The grade of polarity can vary (see next subchapter), but if an expression is even weakly positive or negative, it should be labeled as such. Common positive lexemes might include "elske", "fin", "god", "spennende", and common negative ones might include "hate", "kjedelig", "dum","vanskelig", etc.

<!-- include more about the scopes of polar expressions-->

### Strength
The polarity of a polar expression-target-source tuple varies, and we want to catch that variation to a certain extent. We define three tiers of strengt: strong, standard and slight. Some lexemes might be inherently strongly positive or negative, such as "elske", "hate", "dritt" and "fantastisk", but most will probably be strong/slight due to one or more modifiers. Some examples of these modifiers are "ganske","litt","veldig","ekstremt",kjempe-","sykt","lite","knapt","ikke", and many more. We cannot define what the outcome of these modifiers will be beforehand, it all depends on the context and the inherent polarity and semantics of the polar lexeme if present. Use your intuition: Is the polarity very strong, very slight, or in between.


### Polar expressions in E-FINP sentences
Polar expressions in E-FINP sentences should be marked as well, but this can sometimes be difficult, as there is no definite polar expression in the sentence itself. In these cases, consider what part of the sentence is necessary to understand the evaluation and polarity. In some cases it might be necessary to mark the entire sentence as the polar expression.



### When targets are part of polar expression
One difficult property of targets is that they themselves can be part of sentiment expressions. In some cases it can be difficult to distinguish between when a word is part of a polar expression, and when it is only used as an aspect of the object being evaluated. As mentioned above, we mark only the most general aspect in the sentence, and only if they are canonical. All other possible targets are treated as part of the polar expression. If a sentence contains several canonical aspects, then we allowe nesting. 


### Entities in comparative sentences
Comparative sentences can pose certain challenges. If all entities being compared are present in the sentence, then usually the same polar expression has relations to both targets, often (but not necessarily) with opposite polarities. Comparative sentences can be indicated by the use of comparative adjectival forms, or by the use of adverbs such as "enn" (than). This type of sentences can also be interpreted as the first part of the sentence modfifying the second. Under discussion.
In sentences like
X er bedre enn Y, X and Y are entities, bedre is the polar expression. We say that X er bedre is a polar expression modifying Y, and that "bedre enn Y" is a polar expression modifying X.
X er bra, men Y er bedre.


### Text errrors
In some cases there might be errors in the original document that make annotation difficult. If the sentence still allows for sensible spans, then this should be attempted, otherwise it is ok to leave sentences out if they pose too many problems. Remember that character level spans are disallowed, and therefore we cannot split words in the middle even when it would make sense.


Example:
Frost leder bandet gjennom temposkifter og mer ellermindre avanserte riff

Here, "ellermindre" is written without a space as in "eller mindre". However, the polar expression will still make sense, and therefore it is annotated.

### Suggested steps

-Locate sentences that have been annotated as either E or EFINP at the sentence level. Only these sentences are to be annotated at the fine-grained level.

-Locate the target(s) in the sentence. These are the things that are being talked about. Remember that they should be canonical of the object being reviewed. 

-Find the polar expressions that modify the target. One polar expression might have relations to several targets, in which case brat will ask you to split the polar expression (to create two identical ones), and one target may have relations to several polar expressions.

-If a combination of a polar expression and a canonical target as a whole modifies another target, then these expressions are nested by treating the combination of target and polar expression as one polar expression.

-Lastly, identify the source if present. Thse source is often implicit.

## References

NoReC: The Norwegian Review Corpus ([pdf](http://www.lrec-conf.org/proceedings/lrec2018/pdf/851.pdf))     
Erik Velldal, Lilja Øvrelid, Eivind Alexander Bergem, Cathrine Stadsnes, Samia Touileb and Fredrik Jørgensen   
Proceedings of the 11th edition of the Language Resources and Evaluation Conference, pages 4186–4191  
Miyazaki, Japan, 2018

The good, the bad and the implicit: a comprehensive approach to annotating explicit and implicit sentiment. Marjan Van de Kauter, Bart Desmet, Véronique Hoste. Lang Resources and Evaluation, 2015.([pdf](https://link.springer.com/article/10.1007/s10579-015-9297-4))

Guidelines [link](https://www.lt3.ugent.be/publications/guidelines-for-the-fine-grained-analysis-of-polar-/)
