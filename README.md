# 310-Group-Project

## Project Description 

Our project is going to be an interactive chatbot that takes on the role of a would-be Atlantis explorer. The chatbot will only talk about things regarding Atlantis and will excitedly talk to the user about his upcoming adventure. The link to our GitHub repo is as follows https://github.com/edouarde1/310-Group-Project. 

## How to Run the Chat Bot 

1. Download our GitHub repo 
2. Open the repo using VSCode or Terminal 
3. run `pip install nltk` and `pip install pyspellchecker` in terminal `pip install stanza`
4. Run main.py 

## Dependencies
This bot requires nltk, pyspechecker, and stanza in order to run properly. 

## Dataset 

#### corpus.txt
This txt file is pulled from the [Wikipedia page for Atlantis](https://en.wikipedia.org/wiki/Atlantis). This txt file was used as the corpus for our chat bot.
All these words are tokenized with NLTK and then implemented to a dictionary as keys as a JSON file. 


## Classes and Functions 

### Bot 
This directory includes all the files for the bot. 


### main.py
This is the main file where our program is executed. 

#### get_response(response, keywords)
This function recieves the keyword dictionary, asks for user input, and returns chat bot responses. User input is processed using `get_query_objects()`, which extracts nouns and propper nouns—all while running them through Stanza's dependancy parser. In a for-loop, the loop iterates through each processed noun in a list and detects if the word exists in entity_dict.json. If there is a match, that means there is a chat bot response for the keyword. This response is found using the key-value dictionary pair and is displayed in the GUI. If there is no keyword detected in the user response, then the bot returns "Sorry can't help provide any information that relates to [*whatever related noun the user entered*]". 

  Parameter:
  - response: a string input by the user acting as the key for keywords
  - entity_dict:a .json file generated from entity_dict.py
  
  Returns:
  - output: a string containing the bots response


### main.py 
Main task: This file runs the chat bot. 




