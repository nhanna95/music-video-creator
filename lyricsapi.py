import requests
from apikey import lyrics_search_key

song_name = "thunderstruck"

url = "https://lyrics-search.p.rapidapi.com/search/lyrics"

payload = {"searchTerm": song_name}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": lyrics_search_key,
	"X-RapidAPI-Host": "lyrics-search.p.rapidapi.com"
}

response = requests.request("POST", url, json=payload, headers=headers)

lyrics=response.text
l = lyrics.split(',')
l = l[4:]

print(l)