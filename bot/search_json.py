import json

f = open('./bot/atl_dict.json')
data = json.load(f)

def search_noun_quest(noun, question):
    if noun in data:
        if question in data[noun]:
            return data[noun][question]