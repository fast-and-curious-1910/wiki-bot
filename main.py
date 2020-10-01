# Importing the API Module . Use pip install wikipedia to download and install it.
import wikipedia 

f = open("output_from_wikibot.txt", "w")
search_about = input() # Getting The Input
# Lenght Of Descriptions
short_description = wikipedia.summary(search_about , sentences= 3)
medium_description = wikipedia.summary(search_about, sentences=15)
long_description = wikipedia.summary(search_about, sentences=30)

# Overall Search On Wikipedia
result = wikipedia.search(search_about)
pageonsearch = wikipedia.page(result[0])
# Diffrent Content
categories = pageonsearch.categories
links = pageonsearch.links
content = pageonsearch.content
references = pageonsearch.references
summary = pageonsearch.summary
title = pageonsearch.title




# Writing The Result
print("Page content:\n", content, "\n")
print("Page title:", title, "\n")
print("Categories:", categories, "\n")
print("Links:", links, "\n")
print("References:", references, "\n")
print("Summary:", summary, "\n")
# Or You Can Print these : (Just remove hashtags in front of them and in put hashtags in front of "with open" , code obove this and evrything under it )
#print(medium_description)
#print(long_description)
#print(short_description)




#print(result)
with open("output_from_wikibot.txt", "w" , encoding='utf-8') as f:
    f.write("Page content:\n" + content + "\n")
    f.write("Page title:" + title + "\n")
    f.write("Categories:" + categories + "\n")
    f.write("Links:" + links + "\n")
    f.write("References:" + references + "\n")
    f.write("Summary:" + summary + "\n")
