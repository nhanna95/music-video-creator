from lyricsapi import get_prompts
from tqdm import tqdm
from PIL import Image
import urllib.request
import webbrowser
import random
import openai
import time
import os

openai.organization = 'org-sL2pDmmtVNXIyoV89PpnC6xT'
openai.api_key_path = 'dallekey.txt'

medias = [
    'an oil painting of',
    'a photograph of',
    'a 3D render of',
    'a van gogh style painting of',
    'a hand drawn sketch of',
    'an abstract visual of',
    'an andy warhol style painting of',
    'an oil pastel drawing of',
    'a vaporwave style',
    'a cartoon of',
    'a comic book style drawing of'
]

positive_mood_low_energy = [
    'light',
    'peaceful',
    'calm',
    'serne',
    'soothing',
    'relaxed',
    'placid',
    'comforting',
    'cosy',
    'tranquil',
    'quiet',
    'pastel',
    'delicate',
    'graceful',
    'subtle',
    'balmy',
    'mild',
    'ethereal',
    'elegant',
    'tender',
    'soft',
    'light'
]

positive_mood_high_energy = [
    'bright',
    'vibrant',
    'dynamic',
    'spirited',
    'vivid',
    'lively',
    'energetic',
    'colorful',
    'joyful',
    'romantic',
    'expressive',
    'bright',
    'rich',
    'kaleidoscopic',
    'psychedelic',
    'saturated',
    'ecstatic',
    'brash',
    'exciting',
    'passionate',
    'hot'
]

negative_mood_low_energy = [
    'muted',
    'bleak',
    'funereal',
    'somber',
    'melancholic',
    'mournful',
    'gloomy',
    'dismal',
    'sad',
    'pale',
    'washed-out',
    'desaturated',
    'grey',
    'subdued',
    'dull',
    'dreary',
    'depressing',
    'weary',
    'tired'
]

negative_mood_high_energy = [
    'dark',
    'ominous',
    'threatening',
    'haunting',
    'forbidding',
    'gloomy',
    'stormy',
    'doom',
    'apocalyptic',
    'sinister',
    'shadowy',
    'ghostly',
    'unnerving',
    'harrowing',
    'dreadful',
    'frightful',
    'shocking',
    'terror',
    'hideous',
    'ghastly',
    'terrifying'
]

big_and_free = [
    'curvaceous',
    'swirling',
    'organic',
    'riotous',
    'turbulent',
    'flowing',
    'amorphous',
    'natural',
    'distorted',
    'uneven',
    'random',
    'lush',
    'organic',
    'bold',
    'intuitive',
    'emotive',
    'chaotic',
    'tumultuous',
    'earthy',
    'churning'
]

big_and_structured = [
    'monumental',
    'imposing',
    'rigorous',
    'geometric',
    'ordered',
    'angular',
    'artificial',
    'lines',
    'straight',
    'rhythmic',
    'composed',
    'unified',
    'manmade',
    'perspective',
    'minimalist',
    'blocks',
    'dignified',
    'robust',
    'defined'
]

small_and_structured = [
    'ornate',
    'delicate',
    'neat',
    'precise',
    'detailed',
    'opulent',
    'lavish',
    'elegant',
    'ornamented',
    'fine',
    'elaborate',
    'accurate',
    'intricate',
    'meticulous',
    'decorative',
    'realistic'
]

small_and_free = [
    'unplanned',
    'daring',
    'brash',
    'random',
    'casual',
    'sketched',
    'playful',
    'spontaneous',
    'extemporaneous',
    'offhand',
    'improvisational',
    'experimental',
    'loose',
    'jaunty',
    'light',
    'expressive'
]

song = input('what song would you like: ')

prompts = get_prompts(song)

print('got lyrics')

image_urls = []

for prompt in tqdm(prompts):
    try:
        response = openai.Image.create(
            prompt=medias[random.randint(0, len(medias)-1)] + prompt,
            size="256x256"
        )
        image_urls.append(response['data'][0]['url'])
    except:
        pass
    time.sleep(15)


for url in image_urls:
    webbrowser.open(url)
    time.sleep(5)
