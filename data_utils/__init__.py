import csv 

# Create and reutrn a keywords dict:  dictionary { word1 : bot response1, 
#                                                 word2: bot responnse2,
#                                                 ....    .....     }


def load_data(filename):
    
    with open ("keywords.csv", "r") as file:
        
        bot_dict = dict() 
        
        # Read input from a csv 
        for i, row in enumerate(file):
           
           # Skip column headers 
            if (i == 0):
                continue

            # Construct a dictionary 
            key, value = row.split(",")
            bot_dict[key] = value
        
    return bot_dict

    

    return 0
