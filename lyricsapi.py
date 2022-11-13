from apikey import lyrics_search_key
import requests
import openai
import json
import os


def isnt_space(char):
    return char != ' '


def is_upper(char):
    return char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


url = "https://lyrics-search.p.rapidapi.com/search/lyrics"


def get_prompts(song_name):
    payload = {"searchTerm": song_name}
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": lyrics_search_key,
        "X-RapidAPI-Host": "lyrics-search.p.rapidapi.com"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    try:
        lyrics = response.json()["lyrics"]
    except:
        return []
    verses = lyrics.split('\n\n')
    prompts = []

    for verse in verses:
        bar_sets = []
        ind = 0
        for i in range(len(verse) - 1):
            if isnt_space(verse[i]) and is_upper(verse[i+1]):
                bar_sets.append(verse[ind:i+1])
                ind = i+1

        bar_sets.append(verse[ind:])
        prompts.append(bar_sets)

    final_prompts = []

    for verse in prompts:
        for i in range(int(len(verse)/2)):
            prompt = ' '.join(verse[2 * i:(2 * i) + 2])
            final_prompts.append(prompt)

        if len(verse) % 2 == 1:
            final_prompts.append(verse[-1])

    return final_prompts
