import bot.boty as boty

# Get Bot Dictionary


while True:
    response = input("\n \n Welcome to the Atlantis Chat Bot: \n \n Press 1 to Begin \n \n Press q to Quit \n \n Enter: ")

    # Break and begin bot program 
    if response == '1':
        break

# Bot Program 
while True:
    response = input("\n \n")
    bot_response = boty.get_response(response, keywords)
    if bot_response == 'q':
        print("It was a pleasure talking to you")
        break
    else:
        print(bot_response)
