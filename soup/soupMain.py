import os 
print("WebScrapping 101")
runDefault = input("\nDo you want to run the default mode? YES or NO: ")
if runDefault == "YES":
    os.system('python soupPortal.py')
    os.system('python soupEstudios.py')
    os.system('python soupCS.py')
    os.system('python soupDirectorio.py')

elif runDefault == "NO":
    ask = input("""\nWhich part would you like to run?

    1. soupPortal.py
    2. soupEstudios.py
    3. soupCS.py
    4. soupDirectorio.py

    Enter 1,2,3 or 4:
    """)
    if ask == "1":
        os.system('python soupPortal.py')
    elif ask == "2":
        os.system('python soupEstudios.py')
    elif ask == "3":
        os.system('python soupCS.py')
    elif ask == "4":
        os.system('python soupDirectorio.py')