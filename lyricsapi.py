import requests
from apikey import lyrics_search_key, shrey_key
import os
import openai

song_name = "senorita"

url = "https://lyrics-search.p.rapidapi.com/search/lyrics"

payload = {"searchTerm": song_name}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": lyrics_search_key,
	"X-RapidAPI-Host": "lyrics-search.p.rapidapi.com"
}

response = requests.request("POST", url, json=payload, headers=headers)

lyrics=response.text
lyrics = lyrics.split(",")
lyrics = lyrics[4:]
lyrics = " ".join(lyrics)
lyrics = lyrics.split('\\n\\n')
for verse in lyrics:
  print(verse + "\n")