
from bs4 import BeautifulSoup
import requests,sys,csv,json, os

url="http://ufm.edu/Portal"

# Make a GET request to fetch the raw HTML content
try:
    html_content = requests.get(url).text
except:
    print(f"unable to get {url}")
    sys.exit(1)

# Parse the html content
soup = BeautifulSoup(html_content, "html.parser")

# print if needed, gets too noisy
#print(soup.prettify())

# PRINT retrieved Data
print()
print(""" 
======================================================================
 ___    _                       _ _ _  _  _               
/ __> _| |_ ___  _ _  ___ ._ _ | | | |<_>| | ___ ___ ._ _ 
\__ \  | | / ._>| | |/ ._>| ' || | | || || |<_-</ . \| ' |
<___/  |_| \___.|__/ \___.|_|_||__/_/ |_||_|/__/\___/|_|_|

======================================================================
""")
print("1.Portal\n")

# Print Title:
# print(soup.title)
print("GET the title and print it:",soup.title.string)
print("----------------------------------------------------------------------\n")

# Print Address
address = soup.find_all("a", attrs={"data-toggle":"modal", "href":"#myModal"})

print("GET the Complete Address of UFM:",address[0].text)
print("----------------------------------------------------------------------\n")


# Print phone number & info email:
phoneNumber = soup.find_all("a", attrs={"href":"tel:+50223387700"})
email = soup.find_all("a", attrs={"href":"mailto:inf@ufm.edu"})

print("GET phone number:", phoneNumber[0].text, ", GET email:", email[0].text)
print("----------------------------------------------------------------------\n")

# GET upper nav bar items:
print("GET upper navBar menu:")

for div in soup.find_all("div", attrs={"class":"menu-key"}):
    item = div.text
    newItem = item.replace("\t","").replace("\n","").replace(" ","")
    print(" -",newItem)
print("----------------------------------------------------------------------\n")

# GET all href items
print("GET all href items:")

allHrefs = soup.find_all("a", href=True)

if (len(allHrefs)) > 30:
    print("Output exceeds 30 lines, sending output to:")
    fileName="ALLHrefItems.txt"
    file = open(fileName,"a")
    file.write(f"All hrefs: {allHrefs}")
    file.close
    print(os.path.abspath(fileName))
else:
    for href in allHrefs:
        print(" -", href["href"])
print("----------------------------------------------------------------------\n")

# GET href of "UFMail" button
print("GET href for UFMail button:")

hrefUFMail = soup.find_all("a", href=True, attrs={"id":"ufmail_"})
for href in hrefUFMail:
    print(href["href"])
    print("----------------------------------------------------------------------\n")

# GET href "MiU" button.
print("GET href for MiU button:")

hrefMiU = soup.find_all("a", href = True, attrs={"id":"miu_"})
for href in hrefMiU:
    print(href["href"])
    print("----------------------------------------------------------------------\n")

# GET hrefs of all <img>
print("GET hrefs of all images:")

images = soup.find_all("div", attrs={"class":"imagen"})
for image in images:
    imageHref = soup.find_all("a", href=True)

if len(imageHref) > 30:
    print("Output exceeds 30 lines, sending output to:")

    fileName="AllHrefImages.txt"
    file = open(fileName,"a")
    file.write(f"All hrefs images: {allHrefs}")
    file.close
    print(os.path.abspath(fileName))
else:
    for href in imageHref:
        print(" -",href["href"])
print("----------------------------------------------------------------------\n")

# Count all <a>
a = soup.find_all("a")
aCount = len(a)
print("Count all <a>:", aCount)
print("----------------------------------------------------------------------\n")

