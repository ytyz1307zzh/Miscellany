import spacy
import sys

assert len(sys.argv) == 2, "Cmd Arg: the output filepath"
outpath = sys.argv[1]

paragraph = 'The kangaroo is a marsupial from the family Macropodidae (macropods, meaning "large foot"). ' \
    'In common use the term is used to describe the largest species from this family, the red kangaroo, ' \
    'as well as the antilopine kangaroo, eastern grey kangaroo, and western grey kangaroo.' \
    ' Kangaroos are indigenous to Australia and New Guinea. The Australian government estimates ' \
    'that 42.8 million kangaroos lived within the commercial harvest areas of Australia in 2019, ' \
    'down from 53.2 million in 2013. As with the terms "wallaroo" and "wallaby", "kangaroo" refers to ' \
    'a paraphyletic grouping of species. All three refer to members of the same taxonomic family, ' \
    'Macropodidae, and are distinguished according to size. The largest species in the family are ' \
    'called "kangaroos" and the smallest are generally called "wallabies". The term "wallaroos" ' \
    'refers to species of an intermediate size. There are also the tree-kangaroos, another ' \
    'type of macropod, which inhabit the tropical rainforests of New Guinea, far northeastern' \
    ' Queensland and some of the islands in the region.'

nlp = spacy.load("en_core_web_sm")

raw_textlist = paragraph.strip().split('. ')

outf = open(outpath, 'w', encoding='utf8')
for doc in nlp.pipe(raw_textlist, disable=["ner", "tagger", "parser", "lemmatizer"]):
    sentence_str = ' '.join([token.text for token in doc])
    if not sentence_str.endswith('.'):
        sentence_str += ' .'
    print(sentence_str, file=outf)

outf.close()


