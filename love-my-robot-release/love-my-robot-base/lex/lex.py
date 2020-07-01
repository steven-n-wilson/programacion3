import cozmo, requests, time, os, os.path
from flask import Flask, render_template,request
from cozmo import util, lights
from datetime import datetime


from writePyFile import writeFunc
from stringTo import stringToWrite2


url = "http://localhost:8080/"
app = Flask(__name__)

now = datetime.now()

display = "[ERROR 404] CODE has not RUN or TRANSPILED"

@app.route("/lex",methods =['POST','GET'])
def runLEX():
    global display
    # Get json info 
    # r = requests.get(url)
    # rJSON = r.json()

    # current date and time
    dateTimeObj = now.strftime("%m/%d/%Y, %H:%M:%S")
    
    rDicc = request.get_json()
    print(type(rDicc))
    display, completeName = writeFunc(rDicc)
    name = 'python ' + completeName
    # print(new)
    # print(name)
    os.system(name)

    return render_template("lexRun.html", dateTimeObj=dateTimeObj)

@app.route("/")
def index():
    # r = requests.get(url)
    # rJSON = r.json()

    # current date and time
    dateTimeObj = now.strftime("%m/%d/%Y, %H:%M:%S")

    return render_template("lexGraphicEP.html", dateTimeObj=dateTimeObj, stringToWrite2 = display)


if __name__ == "__main__":
    app.run(host="127.0.0.1",port = 8085, debug=True)