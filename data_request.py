import pandas as pd
import time
import requests
import os
import json
from requests.utils import quote

API_KEY_OMDB = "e67ecccd"  

with open("movie_titles.json", "r", encoding="utf-8") as f:
    movie_titles = json.load(f)


movie_data = []

for title in movie_titles:
    encoded_title= quote(title)
    omdb_url = f"http://www.omdbapi.com/?apikey={API_KEY_OMDB}&t={encoded_title}"
    response = requests.get(omdb_url).json()

    if response.get("Response") == "True":
        movie_data.append({
            "Title": response.get("Title"),
            "Year": response.get("Year"),
            "Rated": response.get("Rated"),
            "Released": response.get("Released"),
            "Runtime": response.get("Runtime"),
            "Genre": response.get("Genre"),
            "Director": response.get("Director"),
            "Writer": response.get("Writer"),
            "Actors": response.get("Actors"),
            "Plot": response.get("Plot"),
            "Language": response.get("Language"),
            "Country": response.get("Country"),
            "Awards": response.get("Awards"),
            "IMDb Rating": response.get("imdbRating"),
            "Metascore": response.get("Metascore"),
            "Box Office": response.get("BoxOffice")
        })
    else:
        print(f"Movie not found: {title} — {response.get('Error')}")
    
    time.sleep(0.5)    

df = pd.DataFrame(movie_data)
df.to_json("omdb_movie_data.json", orient="records", indent=4)
print("Movie data saved to omdb_movie_data.json")
print("Full path:", os.path.abspath("omdb_movie_data.json"))
