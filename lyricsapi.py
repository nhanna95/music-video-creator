import requests
from apikey import lyrics_search_key
import os
import openai
import json


def isnt_space(char):
    return char != ' '


def is_upper(char):
    return char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


song_name = "self care"

url = "https://lyrics-search.p.rapidapi.com/search/lyrics"

payload = {"searchTerm": song_name}
headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": lyrics_search_key,
    "X-RapidAPI-Host": "lyrics-search.p.rapidapi.com"
}

response = requests.request("POST", url, json=payload, headers=headers)

lyrics = response.json()["lyrics"]

verses = lyrics.split('\n\n')

for verse in verses:
    print(verse + '\n\n\n')

exit()


prompts = []

for verse in verses:
    bar_sets = []
    ind = 0
    for i in range(len(verse) - 1):
        if isnt_space(verse[i]) and is_upper(verse[i+1]):
            bar_sets.append(verse[ind:i+1])
            ind = i+1

    prompts.append(bar_sets)

final_prompts = []

for verse in prompts:
    for i in range(int(len(verse)/2)):
        prompt = ' '.join(verse[2 * i:(2 * i) + 2])
        final_prompts.append(prompt)

for prompt in final_prompts:
    print(prompt + '\n')
