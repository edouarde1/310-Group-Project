import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import stanza
def data_load(filepath):
    with open (filepath,'r', errors='ignore') as file:
        contents = file.read()
    return contents


def preproc(filepath):
    file_contents = data_load(filepath)
    sentences = nltk.sent_tokenize(file_contents)
    sentences = [(sent) for sent in sentences]
    return sentences


# POS TAGGING INPUT: LIST OF SENTENCES
def pos_tagger(sentences): 
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    sentences = [nltk.pos_tag(sent) for sent in sentences]
    return sentences

# DEPENDENCYPARSER, INPUT: String 
def dependencyParser(sentence):
    
    # Stanza 
    nlp = stanza.Pipeline(lang='en', processors='tokenize,mwt,pos,lemma,depparse')

    # Return query
    return nlp(sentence)



