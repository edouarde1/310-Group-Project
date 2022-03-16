from data_utils.data_load import preproc, pos_tag, dependencyParser, get_query_objects
from data_utils.entity_dict import create_entity_dict,get_entity_dict
import nltk
import json
import stanza 

#TEXT_BODY_PATH = 'bot/text/atlantis.txt'
ENTITY_DICT_PATH = 'bot/entity_dict.json'
entity_dict = get_entity_dict(ENTITY_DICT_PATH)

query = " Tell me about atlantis ?"



def get_response(query, entity_dict):
    
    response = []
    # Find the objects in the user query 
    query_objects = get_query_objects(query)


    for obj in query_objects:
        
        if obj in entity_dict:
            response.append(entity_dict[obj])
        else:
            print("Sorry can't help provide any information that relates to " + obj)
    
    return " ".join(response)
        
resp = get_response(query, entity_dict)

print(resp)



