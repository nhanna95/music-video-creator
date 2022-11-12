from apikey import key
from PIL import Image
import urllib.request
import webbrowser
import openai
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

response = openai.Image.create(
    prompt="an oil painting of a group of human-like androids sitting at a cocktail bar",
    size="256x256"
)
image_url = response['data'][0]['url']

webbrowser.open(image_url)
