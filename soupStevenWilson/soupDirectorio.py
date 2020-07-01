from bs4 import BeautifulSoup
import requests, re , sys, csv, json, os

url = "https://www.ufm.edu/Directorio"

# GET raw html content
try: 
    html_content = requests.get(url).text

except:
    print(f"Unable to get: {url}")
    sys.exit(1)

# Parse the htlm content
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
print("4. Directorio\n")

# Sort all emails alphabetically
print("Sort all emails alphabetically:")
emails = []

table = soup.find_all("table", attrs={"class":"tabla ancho100"})
for element in table:
    tableRow = element.find_all("tr")
    for item in tableRow:
        closer = item.find_all("a", href = True, attrs={"class":"external text"})
        for href in closer:
            decide = href["href"]
            for a in decide:
                if a == "@":
                    mailto = decide.replace("mailto:", "")
                    emails.append(mailto)
                    emails.sort()

if len(emails) > 30:
    print("Output exceeds 30 lines sending to..")

    fileName="emailsAlphabeticallysSoupDirectory.txt"
    file = open(fileName,"a")
    file.write(f"All emails: {emails}")
    file.close

    print(os.path.abspath(fileName))
    print("----------------------------------------------------------------------\n")
else:
    for email in emails:
        print(" -", email)

# Count all emails that start with a vowel.
emailsVowel = []
for email in emails:
    if email[0] in "aeiou":
        emailsVowel.append(email)

print("Count all emails that start with vowel:", len(emailsVowel))
print("----------------------------------------------------------------------\n")

# GET the directory of all 3 column table and generate a CSV with these columns 

table = soup.find_all("table", attrs={"class":"tabla ancho100 col3"})
tableCSV= []

# Create a file to write to, add headers row
f = csv.writer(open("directorio.csv", 'w'))
f.writerow(["Role", "Name"])

for data in table:
    tr = data.find_all("tr")
    for item in tr:
        td = item.find_all("td")
        for text in td:
            tableCSV.append(text.text)

f.writerow([tableCSV])




