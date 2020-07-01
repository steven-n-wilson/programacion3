from flask import Flask, jsonify, render_template, request
import os, optparse, requests, json

bio = Flask(__name__)

developer = os.getenv("DEVELOPER", "Steven Wilson")
environment=os.getenv("ENVIRONMENT","development")

response = requests.get('https://api.themoviedb.org/3/trending/movie/week?api_key=c2fd774870d4a09046deebc36f861d7d')
data = response.json()
print(data["results"][0]["title"])
with open('trendingMoviesAPI.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

@bio.route("/")
def home():
    return render_template("layout.html",
    data = data,
    webTitle = "Love My Movies",
    webSubtitle = "Trending Movies",

    appBox1Title = data["results"][0]["title"], 
    appBox1Subheading = data["results"][0]["release_date"],
    appBox1ContentText = data["results"][0]["overview"], 

    appBox2Title = data["results"][1]["title"], 
    appBox2Subheading = data["results"][1]["release_date"],
    appBox2ContentText = data["results"][1]["overview"], 

    appBox3Title = data["results"][2]["title"], 
    appBox3Subheading = data["results"][2]["release_date"],
    appBox3ContentText = data["results"][2]["overview"], 

    appBox4Title = data["results"][3]["title"], 
    appBox4Subheading = data["results"][3]["release_date"],
    appBox4ContentText = data["results"][3]["overview"], 

    some_value = True,
    developer = developer)

if __name__ == "__main__":
    debug=False
    if environment == "development" or environment == "local":
        debug=True
    bio.run(host="127.0.0.2",debug=debug)