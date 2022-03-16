from data_utils.data_load import preproc
from data_utils.data_load import get_query_objects
import json

def create_entity_dict(filepath):
    with open('bot/entity_dict.json', 'w') as file:
        contents = preproc(filepath)
        obj_dict = dict()
    
    # Retreive nouns from each sentence 
        for sent in contents:
            objs = get_query_objects(sent)
            if (objs != None):
                for i,obj in enumerate(objs):
                    obj_dict[obj.lower()] = sent
        file.write(json.dumps(obj_dict))  

def get_entity_dict(path_to_json):
    with open (path_to_json) as json_file:

        entity_dict = json.load(json_file)

    return entity_dict

