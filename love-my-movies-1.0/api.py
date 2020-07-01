import requests, json 

response = requests.get('https://api.themoviedb.org/3/trending/movie/week?api_key=c2fd774870d4a09046deebc36f861d7d')
data = response.json()


with open('trendingMoviesAPI.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)