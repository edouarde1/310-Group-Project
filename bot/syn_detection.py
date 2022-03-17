from nltk.corpus import wordnet


def detect_syn(input):
    synonyms = []
    # This first loop iterates through all of the synsets that are associated with our input using wordnet.
    for syn in wordnet.synsets(input):
        # Then, also using word net it iterates through all of the words that are under that synset. We append that to a list and get our list of synonyms.
        for i in syn.lemmas():
            synonyms.append(i.name())
    return synonyms
