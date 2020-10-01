from bs4 import BeautifulSoup
import requests
import string
import sys

# All The Variables
enter_input = input("Search: ")
f = open("data.txt", "x")
u_i =  string.capwords(enter_input)
lists = u_i.split()
word = "_".join(lists)
url = "https://en.wikipedia.org/wiki/"+word
url_open = requests.get(url)
soup = BeautifulSoup(url_open.content, 'html.parser')
details = soup('table', {'class': 'infpox'})

def wikibot(url):
    url_open = requests.get(url)
    soup = BeautifulSoup(url_open.content,'html.parser')
    details = soup('table',{'class':'infpox'})
    for i in details:
        h = i.find_all('tr')
        for j in h:
            heading = j.find_all('th')
            detail = j.find_all('td')
            if heading is not None and detail is not None:
                for x,y in zip(heading,detail):
                    f.write("{} :: {}".format(x.text,y.text))
                    f.write("--------------------------")



paragraphs = soup.find_all('p')
for paragraph in paragraphs:
    sys.stdout.write(paragraph.text + '\n')
wikibot(url)
