from bs4 import BeautifulSoup
import requests, sys, csv, json

url = "http://ufm.edu/Estudios"

# GET raw html content
try:
    html_content = requests.get(url).text
except:
    print(f"Unable to get {url}")
    sys.exit(1)

# Parse the html content
soup = BeautifulSoup(html_content, "html.parser")

# PRINT DATA ---------------------------------------------------------------------
print()
print(""" 
======================================================================
 ___    _                       _ _ _  _  _               
/ __> _| |_ ___  _ _  ___ ._ _ | | | |<_>| | ___ ___ ._ _ 
\__ \  | | / ._>| | |/ ._>| ' || | | || || |<_-</ . \| ' |
<___/  |_| \___.|__/ \___.|_|_||__/_/ |_||_|/__/\___/|_|_|

======================================================================
""")
print("2.Estudios\n")

# GET Estudios href
estudiosURL = soup.find("meta", property = "og:url")
print("Obtain Estudios URL:", estudiosURL["content"])
print("----------------------------------------------------------------------\n")

# Display all items from top menu (8 items)
print("Top Menu items:")
for div in soup.find_all("div", attrs={"class":"dsuperior"}):
    text = div.text
    cleanText = text.replace(" ","")

    finalText = cleanText.split("\n")
    finalText.remove("")
    finalText.remove( '')

    for item in finalText:
        print(" -",item)
print("----------------------------------------------------------------------\n")

# Display ALL "Estudios" (Doctorados/Maestrias/Posgrados/Licenciaturas/Baccalaureus)
print("Display all 'Estudios':")
estudios = soup.find_all("div", attrs={"class":"estudios"})
for div in estudios:
    print(" -", div.text)
print("----------------------------------------------------------------------\n")

# Display ALL items from leftbar:
print("Display all 'leftbar' items:")
divLeftbar = soup.find_all("div", attrs={"class":"leftbar"})
for div in divLeftbar:
    text = div.find_all("a")
for items in text:
        print(" -",items.text)
print("----------------------------------------------------------------------\n")

# Display all available social media (href):
print("Display all available social media links:")
divSocial = soup.find_all("div", attrs={"class":"social pull-right"})
for div in divSocial:
    hrefSocial = div.find_all("a", href = True)
    for href in hrefSocial:
        print(" -",href["href"])
print("----------------------------------------------------------------------\n")

# Count all "a":
a = soup.find_all("a")
aCount = len(a)
print("Count all <a>", aCount)
print("----------------------------------------------------------------------\n")





