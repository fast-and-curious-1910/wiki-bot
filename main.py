# Importing the API Module . Use pip install wikipedia to download and install it.
# I have commented out stuff which I dont need , but you might need it just remove # and it will be a normal function
import wikipedia 
import webbrowser
import time 


f = open("output_from_wikibot.txt", "w")
print("Enter Search Term:")
search_about = input() # Getting The Input
print("Getting Data ... Please wait .... see the output_from_wikibot.txt for data as well")


# Lenght Of Descriptions
short_description = wikipedia.summary(search_about , sentences= 3)
medium_description = wikipedia.summary(search_about, sentences=15)
long_description = wikipedia.summary(search_about, sentences=30)

# Overall Search On Wikipedia
result = wikipedia.search(search_about)
pageonsearch = wikipedia.page(result[0])
# Diffrent Content



# Printing The Result

print("Page title:", title, "\n")
print("Categories:", categories, "\n")
#print("Links:", links, "\n")
#print("References:", references, "\n")
print("Summary:", summary, "\n")


# Or You Can Print/Write these : (Just remove hashtags in front of them and in put hashtags in front of "with open" 👇 , code obove this 👆 and evrything under it )
#print(medium_description)
#print(long_description)
#print(short_description)
#f.write(medium_description)
#f.write(long_description)
#f.write(short_description)



# Writing To /output_from_wikibot.txt 
with open("output_from_wikibot.txt", "w" , encoding='utf-8') as f:
    f.write("Page content:\n" + content + "\n")
    f.write("Page title:" + title + "\n")
    #f.write("Categories:" + categories + "\n")
    #f.write("Links:" + links + "\n")
    #f.write("References:" + references + "\n")
    f.write("Summary:" + summary + "\n")





## Please subscribe to my YouTube channel 
my_channel = "PalPalash"
print("Please subscribe to my channel " + my_channel + " on Youtube")

webbrowser.open('https://www.youtube.com/channel/UCdfaHl9USu-J-kp4Bj_7J2Q?sub_confirmation=1', new=2)


print("Quitting Now")
quit()

