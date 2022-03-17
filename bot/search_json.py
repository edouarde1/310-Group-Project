import json

f = open('./bot/atl_dict.json')
data = json.load(f)

def search_noun_quest(noun, question):
    if noun in data:
        if question in data[noun]:
            return data[noun][question]
def get_nouns():
    nounList = []
    for noun in data:
        nounList.append(noun)
    return nounList
print(get_nouns())