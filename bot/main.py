from data_utils.data_load import preproc, pos_tag, dependencyParser
import re, pprint
import nltk
import stanza 
import os 



# POS TAGGING 
TEXT_BODY_PATH = './text/atlantis.txt'

# Retrieve preprocess sentences
sentences = preproc(TEXT_BODY_PATH)
sentences = pos_tag(sentences)
print(sentences)



# Sentence relationships 








# Queury Similar words from text body
text = nltk.Text(str(list(zip(word))[0]).strip('(').strip(')').strip('\',').lower() for sent in sentences for word in sent)

text.similar('captial')


def process_query(string): 
    # Retu
    dp_query = dependencyParser("Will I need a ship to go to atlantis?")
    for sent in dp_query.sentences:
        for word in sent.words:
            if word.deprel == "obj" or word.deprel == "":
                print(word.text)
