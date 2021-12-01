from allennlp_models import pretrained

# predictor = Predictor.from_path("https://storage.googleapis.com/allennlp-public-models/bert-base-srl-2020.11.19.tar.gz")
predictor = pretrained.load_predictor("structured-prediction-srl-bert")

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

sentence_list = paragraph.strip().split('. ')

for s in sentence_list:
    tree = predictor.predict(sentence=s)
    value = predictor.dump_line(tree)
    print(value)


