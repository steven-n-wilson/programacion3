from datetime import datetime
import os.path
from stringTo import stringToWrite2


def writeFunc(rDicc):
    try: 
        global new

        now = datetime.now()
        date_time = now.strftime("lmr_LEX_%m-%d-%Y_%H-%M-%S")
        print("File Name:",date_time +".py")

        path = "lex/transpiled/"
        fileName = str(date_time) + ".py"

        completeName = os.path.join(path, fileName)

        rDicc = str(rDicc)
        # print(rDicc)
        new = stringToWrite2.format(rDicc)

        f = open(completeName, "w")
        f.write(new)
        f.close()

        return new, str(completeName)

    except:
        return