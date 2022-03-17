import csv


# Create and return a keyword dict:  dictionary { word1 : bot response1,
#                                                 word2: bot response2,
#                                                 ....    .....     }
def load_data(filename):
    try:
        with open(filename, "r", encoding="utf-8", errors="ignore") as file:
            bot_dict = dict()

            # Read input from a csv 
            csv_contents = csv.reader(file, delimiter=",")

            for i, row in enumerate(csv_contents):
                # Ignor Headers
                if i == 0:
                    continue

                bot_dict[row[0]] = row[1]
    except FileNotFoundError:
        return "Sorry! I cant come up with the words right now"
    return bot_dict
            



def get_response(response, keywords):
    reponse_array = response.lower().split(" ")
    # q quits program
    if response == 'q':
        return 'q'

    match = False

    for i, word in enumerate(reponse_array):

        # Match, then print reponse
        if word in keywords:
            match = True
            return "\n \n" + keywords[word]
            # No Match, no longer iterating, default
    if not match:
        return "Sorry I did not understand what you said"
