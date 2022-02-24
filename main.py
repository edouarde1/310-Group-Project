from naive_bot import load_data

# Get Bot Dictionary
keywords = load_data("keywords.csv")

while True:
    response = input("\n \n Welcome to the Atlantis Chat Bot: \n \n Press 1 to Begin \n \n Press q to Quit \n \n Enter: ")

    # Break and begin bot program 
    if response == '1':
        break

# Bot Program 
while True: 
    response = input("\n \n")

    reponse_array = response.lower().split(" ")

    # q to quit program 
    if response == 'q':
        break 
    
    match = False

    for i, word in enumerate(reponse_array):

        # Match, then print reponse 
        if word in keywords:
            print("\n \n" + keywords[word])
            match = True
            break 
    
    # No Match, no longer iterating, default 
    if not match:
        print("Sorry I did not understand what you said")

       

    
    