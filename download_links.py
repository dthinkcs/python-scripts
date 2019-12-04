from bs4 import BeautifulSoup, SoupStrainer
import requests
import sys

if len(sys.argv) < 1:
    print("Invalid Entry")
    exit()

url = sys.argv[1]
tempurl = url.replace("//", "")
baseurl = tempurl[:tempurl.find("/")]
print(baseurl)


page = requests.get(url)    
data = page.text
soup = BeautifulSoup(data)

for link in soup.find_all('a'):
    if link.get('href'):
        if link.get('href')[0] == "/": 
            print(baseurl + link.get('href'))
        else:
            print(link.get('href'))


# Full url:
# http://stackoverflow.com/questions/6038061/regular-expression-to-find-urls-within-a-string

# Base:

# stackoverflow.com

# Regex:
# (http(s)?:\/\/)|(\/.*){1}

# Example in JavaScript:

# function toBaseURL(fullURL){
#     return fullURL.replace(/(http(s)?:\/\/)|(\/.*){1}/g, '');
# }