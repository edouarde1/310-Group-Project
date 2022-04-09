import wikipediaapi as wapi

#Setting the language, the WIKI can be changed to HTML to output in HTML format.
wiki = wapi.Wikipedia( language = 'en', extract_format=wapi.ExtractFormat.WIKI)

#Creating a page

input = "Define atlantis"
pageName = input.replace("Define ", "", 1)
page = wiki.page(pageName.lower())
if page.exists:
    summ = page.summary[0:1000].replace(". ", "\n", 1).splitlines()
    print(summ[0] + ".\nThe link for the full wikipedia article is " + page.fullurl)
else:
    print("This page does not exist.")


#Checking if a page exists
#print("Page - Exists: %s" %page.exists())

#Getting a title
#print("Page - Title: %s" % page.title)

#Getting a summary, the square brackets set the character count
#print("Page - Title: %s" % page.summary[0:61])

#Getting the URL
#print(page.fullurl)

#This prints out the entire page.
#print(page.text)

#Section Printer
def print_sections(sections, level=0):
    for s in sections:
        print("%s: %s - %s" % ("*" * (level+1), s.title, s.text[0:40]))
        print_sections(s.sections, level+1)

#print_sections(page.sections)

#Printing out page categories
def print_categories(page):
    categories = page.categories
    for title in sorted(categories.keys()):
        print("%s: %s" % (title, categories[title]))

#print_categories(page)