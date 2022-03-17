import search_json
from data_utils.data_load import get_query_objects
from spellchecker import SpellChecker
import random

TEXT_BODY_PATH = './text/atlantis.txt'
ENTITY_DICT_PATH = 'data_utils/entity_dict.json'

responses = ["I'm sorry, I don't understand.",
             "I am unsure what you are asking me.",
             "Sorry, I only want to talk about Atlantis and Treasure",
             "Ask me about Atlantis or Treasure.",
             "Your words make no sense to me.",
             "I know nothing about that topic."]


def spell_check(input):
    # takes a string and returns a list substring of corrected words
    spell = SpellChecker()
    err = input.split()
    correct = []
    for word in err:
        word = spell.correction(word)
        correct.append(spell.correction(word))
    return " ".join(correct)


def get_response(query):
    # entity_dict = get_entity_dict(ENTITY_DICT_PATH)
    #
    # response = []
    # Find the objects in the user query
    query_objects = get_query_objects(query)
    if query_objects is None:
        return responses[random.randint(0, len(responses)-1)]
    else:
        response = search_json.search_noun_quest(query_objects[0], query_objects[1])
    # for obj in query_objects:
    #
    #     if obj in entity_dict:
    #         response.append(entity_dict[obj])
    #     else:
    #         # Satisfies 5 possible responses for out of topic questions
    #         return responses[random.randint(0, len(responses))]

    return " ".join(response)
