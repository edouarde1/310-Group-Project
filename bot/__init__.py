
from contextlib import nullcontext
from naive_bot.naive_bot import load_data
    
def atlantis_bot():
    def __init__(self):
        self.name = "Indiana Bones"
        self.dict = load_data("/keywords.csv")

    def respond(self, str_input):
        words = str_input.lower().split()
        for word in words:
            if word in self.dict.keys():
                return self.dict[word]
        return "I'm sorry, I don't understand."

    

