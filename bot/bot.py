import random
from naive_bot.naive_bot import load_data

responses = ["I'm sorry, I don't understand.",
             "I am unsure what you are asking me.",
             "Sorry, I only want to talk about Atlantis and Treasure",
             "Ask me about Atlantis or Treasure.",
             "Your words make no sense to me.",
             "I know nothing about that topic."]


class bot:
    def __init__(self):
        self.name = "Indiana Bones"
        self.dict = load_data("/keywords.csv")

        def respond(self, str_input):
            words = str_input.lower().split()
            for word in words:
                if word in self.dict.keys():
                    return self.dict[word]
            # Satisfies 5 possible responses for out of topic questions
            return responses[random.randint(0, len(responses))]

        def test(self):
            print("Hot Damn, this actually works!")
