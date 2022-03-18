import json
import sys
import os

try:
    f = open('bot/atl_dict.json')
    data = json.load(f)
except:
    current = os.path.dirname(os.path.realpath(__file__))
    print(os.listdir(os.curdir))
def search_noun_quest(noun, question):
    if noun in data:
        if question in data[noun]:
            return data[noun][question]


def get_nouns():
    nounList = []
    for noun in data:
        nounList.append(noun)
    return nounList


def get_questions(noun):
    questList = []
    for question in data[noun]:
        questList.append(question)
    return questList
