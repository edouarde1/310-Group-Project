from data_utils.data_load import preproc
from data_utils.data_load import get_query_objects
import json

"""
The chat bot uses a dictionay structure in  order to extract information about topics 
selected by the user. This file creates the dictionary from any body of text. The dicionary 
uses nouns and proper nouns as keys and sentences as values. The idea is that the when 
the  user types a query the objects (Nouns and Proper Nouns) will potentially match with an  
object in the entity dictionary, that is created here. 
"""


def create_entity_dict(filepath):
    """
Creates the dictionary from a body of text and outputs dictionary into a json file called 
'entity_dict.json'. The file contents are preprocessed and recieved. Iterating though each sentece,
nouns from the sentece are extracted as keys and completed sentence where  nouns reside in are 
used as values. 

PARAMETERS: 
    filepath: path to json file

RETURNS:
   None
    """
    with open('bot/entity_dict.json', 'w') as file:

        #Preprocessing of the file 
        contents = preproc(filepath)
        obj_dict = dict()
    
        #Iterate through each sentence
        for sent in contents:
              #Retreive entities from the each sentence 
            objs = get_query_objects(sent)
            if (objs != None):
                for i,obj in enumerate(objs):
                    obj_dict[obj.lower()] = sent
        file.write(json.dumps(obj_dict))  

def get_entity_dict(path_to_json):
    """
Retrieves the entity dictionary from a json file

PARAMETERS:
    path_to_json: path to the json file 

RETURNS: 
    entity_dict: a dictionary of keywords { entity1: sentenceX
                                            entity2: sentenceX
                                            ..     : .. 
                                                              }
    """
    with open (path_to_json) as json_file:
        # Load the dictionary
        entity_dict = json.load(json_file)

    return entity_dict

