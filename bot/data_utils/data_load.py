import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import stanza

# Pipeline object to access token, mwt, lemma, and depparse functions from Stanza
NLP = stanza.Pipeline(lang='en', processors='tokenize,mwt,pos,lemma,depparse', verbose=False)

def data_load(filepath):
    """
Loads text from a file

PARAMETERS:
    filepath: file to path to retrieve text from 

RETURNS:
    contents: string of raw text
    """

    with open (filepath,'r', errors='ignore') as file:
        contents = file.read()
    return contents


def preproc(filepath):
    """
Preprocess a body of text using sentence tokenization from nltk

PARAMETERS:
    filepath : path to .txt that contains word corpur

RETURN:
    None
    """

    file_contents = data_load(filepath)
    sentences = nltk.sent_tokenize(file_contents)
    for sent in sentences:
        word_tokens = []
        for word in sent:
            word_tokens.append(str(nltk.word_tokenize(word)))
        sent = ' '.join(word_tokens)
        
    return sentences

def pos_tagger(sentences): 
    """
Part-of-speech tagger utility using nltk

PARAMETERS:
    sentences: List[] of sentences 

RETURNS:
    sentences: a nested List[] of sentences where each sentence is represented as a list of 
    tuples (word,pos)
    """
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    sentences = [nltk.pos_tag(sent) for sent in sentences]
    return sentences


def get_query_objects(query): 
    """
Extracts the nouns and proper pouns from the user query. Takes a user query and runs string 
through Stanza's Dependency Parser. More information about this library is found here: 
https://stanfordnlp.github.io/stanza/depparse.html

PARAMETERS:
    query: a string 

RETURNS:
    obj_list: a list nouns and proper nouns from the user query 
    """
    # Find out sentence dependencies
    dp_query = dependencyParser(query)
   
    # Filter out only obects (NOUNs) from the user query 
    obj_list = []
    for sent in dp_query.sentences:
        for word in sent.words:
            if word.upos == "NOUN" or word.upos == "PROPN":
                obj_list.append(word.text)

    return obj_list

# DEPENDENCYPARSER, INPUT: String 
def dependencyParser(sentence):
    """
Helper utility used to extract the depencies from a sentence. Runs the dp pipeline object 
in order to run depparse, lemma, and pos tagginig.

PARAMETERS:
    sentence: a string 

    """
    # Return depencies 
    return NLP(sentence)






    
