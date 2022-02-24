import csv 

# Create and reutrn a keywords dict:  dictionary { word1 : bot response1, 
#                                                 word2: bot responnse2,
#                                                 ....    .....     }


def load_data(filename):
    with open ("keywords.csv", "r", encoding="utf-8", errors="ignore") as file:
        bot_dict = dict() 
        
        # Read input from a csv 
        csv_contents = csv.reader(file, delimiter = ",")
        
        for i, row in enumerate(csv_contents):
            # Ignor Headers
            if i == 0:
                continue
         
            bot_dict[row[0]] = row[1]
            
    return bot_dict

    

