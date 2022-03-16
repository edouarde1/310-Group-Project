import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import stanza

NLP = stanza.Pipeline(lang='en', processors='tokenize,mwt,pos,lemma,depparse')

def data_load(filepath):
    with open (filepath,'r', errors='ignore') as file:
        contents = file.read()
    return contents


def preproc(filepath):
    file_contents = data_load(filepath)
    sentences = nltk.sent_tokenize(file_contents)
    print(sentences)
    for sent in sentences:
        word_tokens = []
        for word in sent:
            word_tokens.append(str(nltk.word_tokenize(word)))
        sent = ' '.join(word_tokens)
        
    return sentences


# POS TAGGING INPUT: LIST OF SENTENCES
def pos_tagger(sentences): 
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    sentences = [nltk.pos_tag(sent) for sent in sentences]
    return sentences


def get_query_objects(query): 
    
    # Find out sentence dependencies
    dp_query = dependencyParser(query)
    print(dp_query)
    # Filter out only obects (NOUNs) from the user query 
    obj_list = []
    for sent in dp_query.sentences:
        for word in sent.words:
            if word.upos == "NOUN" or word.upos == "PROPN":
                obj_list.append(word.text)

    return obj_list

# DEPENDENCYPARSER, INPUT: String 
def dependencyParser(sentence):

    # Return depencies 
    return NLP(sentence)






    
