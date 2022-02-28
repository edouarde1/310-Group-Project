# 310-Group-Project

## Project Description 

Our project is going to be an interactive chatbot that takes on the role of a would-be Atlantis explorer. The chatbot will only talk about things regarding Atlantis and will excitedly talk to the user about his upcoming adventure. The link to our GitHub repo is as follows https://github.com/edouarde1/310-Group-Project. 

## How to Run the Chat Bot 

1. Download our GitHub repo 
2. Open the repo using VSCode or Terminal 
3. Run main.py 

## Classes and Functions 

### Naive Bot 
This directory includes all the files for the naive bot. All other directories can be ignored as they will be used for future developments on the chat bot 

#### __init.py___ 
Main Task: This file includes all the naive bot functionality. 

load_data(filename)
This function creates a dictionary structure for the chat bot by iterating through a csv file. The keys are words, and the values are responses. For example, the key "Hey" has a value of "Hail and well met strange traveler!". This key-value correlation is how the chat bot responds to user inputs.

  Parameter:
  filename- Path to a csv file that holds key value pairs 

  Return: 
  bot_dict- Keyword dictionary for the key-value pairs

### main.py 
Main task: This file runs the chat bot. 

It retrieves the keyword dictionary, displays user menu, asks for user input, and returns chat bot responses. The user input is converted into a list a of words using a space delimiter. In a for-loop, the loop iterates through each word in the list and detects if the word exists in the keyword dictionary. If there is a match, that means there is a chat bot response for the keyword. This response is found using the key-value dictionary pair and is displayed in the terminal window. If there is no keyword detected in the user response, then the bot returns "Sorry I did not understand what you said". The user can quit the chat bot by pressing 'q'. This terminates the while loop and kills the program.



