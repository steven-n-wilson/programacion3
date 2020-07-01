#FLASK
from __future__ import print_function
import yaml 

from flask import Flask, jsonify, render_template, request
import os,optparse
import yaml
app = Flask(__name__)

developer = os.getenv("DEVELOPER", "Steven Wilson")
environment=os.getenv("ENVIRONMENT","development")

@app.route("/")
def home():
    foo="bar"
    return render_template("home.html", mivariable=foo ,developer=developer)

@app.route("/aboutMe")
def aboutMe():
    # mydata = yaml.dump("info.yml")
    data = yaml.load(open("info.yml"))
    myData = yaml.dump(data, default_flow_style=False)
    return render_template("aboutMe.html", myData=myData)

@app.route("/education")
def education():
    return render_template("education.html")


@app.route("/workExperience")
def workExperience():
    foo="bar"
    return render_template("workExperience.html", mivariable=foo ,developer=developer)

if __name__ == "__main__":
    debug=False
    if environment == "development" or environment == "local":
        debug=True
    app.run(host="127.0.0.1",debug=debug)

