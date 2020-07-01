from bs4 import BeautifulSoup
import requests, re, sys, csv, json, urllib.request

url = "https://fce.ufm.edu/carrera/cs/"

# GET raw html content
try: 
    html_content = requests.get(url).text
except:
    print(f"Unable to get: {url}")
    sys.exit(1)

# Parse the html content
soup = BeautifulSoup(html_content, "html.parser")

# Print Data -----------------------------------------------------
print()
print(""" 
======================================================================
 ___    _                       _ _ _  _  _               
/ __> _| |_ ___  _ _  ___ ._ _ | | | |<_>| | ___ ___ ._ _ 
\__ \  | | / ._>| | |/ ._>| ' || | | || || |<_-</ . \| ' |
<___/  |_| \___.|__/ \___.|_|_||__/_/ |_||_|/__/\___/|_|_|

======================================================================
""")
print("3. CS\n")

# GET Title
# print(soup.title)
print("GET title:",soup.title.string)
print("----------------------------------------------------------------------\n")

# GET CS url:
csURL = soup.find("meta", property = "og:url")
print("GET CS URL:",csURL["content"])
print("----------------------------------------------------------------------\n")

# Download "FACULTAD de CIENCIAS ECONOMICAS" logo. 
print("DOWNLOAD 'FACULTAD de CIENCIAS ECONOMICAS' logo:\n")

def downloader(URL):
    fileName = input("\nSave File As:")
    fullFileName = str(fileName) + '.png'
    urllib.request.urlretrieve(URL,fullFileName)
    print("Image saved as :", fullFileName)
    print("File saved at Github Repository")

aFCE = soup.find_all("a", attrs={"href":"https://fce.ufm.edu"})

decide = input("Do you want to download the image? Enter YES or NO: ")

if decide == "YES":
    for a in aFCE:
        image = a.find("img", attrs={"class":"fl-photo-img wp-image-500 size-full"})
        imageURL = image["src"]
        print("Image SRC link:",imageURL)
        downloader(imageURL)
        print("----------------------------------------------------------------------\n")

elif decide =="NO":
    print("----------------------------------------------------------------------\n")

# GET Title and Description
print("GET title:",soup.title.string)
description = soup.find("meta", property = "og:description")
print("\nGET Description:",description["content"])
print("----------------------------------------------------------------------\n")

# Count al "a":
a = soup.find_all("a")
aCount = len(a)
print("Count all <a>", aCount)
print("----------------------------------------------------------------------\n")


# Count all "a":
div = soup.find_all("div")
divCount = len(div)
print("Count all <div>", divCount)
print("----------------------------------------------------------------------\n")







