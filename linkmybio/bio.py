from flask import Flask, jsonify, render_template, request
import os, optparse, yaml

bio = Flask(__name__)

developer = os.getenv("DEVELOPER", "Steven Wilson")
environment=os.getenv("ENVIRONMENT","development")

data = yaml.load(open("links.yaml"))

@bio.route("/")
def home():
    return render_template("info.html", data = data,
    picture = data["picture"],
    name = data["name"],
    shortbio = data["shortbio"],
    
    fbEnable = data["links"][0]["facebook"]["enable"],
    fbLink = data["links"][0]["facebook"]["link"],
    fbDescription = data["links"][0]["facebook"]["description"],
    
    igEnable = data["links"][1]["instagram"]["enable"],
    igLink = data["links"][1]["instagram"]["link"],
    igDescription = data["links"][1]["instagram"]["description"],

    blogEnable = data["links"][2]["blog"]["enable"], 
    blogLink = data["links"][2]["blog"]["link"],
    blogDescription = data["links"][2]["blog"]["description"],

    gitHubLinkEnable = data["links"][3]["gitHub"]["enable"],
    gitHubLink = data["links"][3]["gitHub"]["link"],
    gitHubDescription = data["links"][3]["gitHub"]["description"],

    
    some_value = True,
    developer = developer)


if __name__ == "__main__":
    debug=False
    if environment == "development" or environment == "local":
        debug=True
    bio.run(host="127.0.0.1",debug=debug)
