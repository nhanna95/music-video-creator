import os
import openai
from apikey import shrey_key, dalle_key

openai.api_key_path='apikey.txt'
openai.api_key = os.getenv(openai.api_key_path)

response = openai.Completion.create(
  model="text-davinci-002",
  prompt="Extract keywords from this text:\n\n['\"lyrics\":\"Thunder', ' thunder', ' thunder', ' thunderThunder', ' thunder', ' thunder', ' thunderThunder', \" thunder\\\\n\\\\nI was caughtIn the middle of a railroad track (thunder)I looked 'roundAnd I knew there was no turning back (thunder)My mind racedAnd I thought\", ' what could I do? (Thunder)And I knewThere was no help', \" no help from you (thunder)Sound of the drumsBeating in my heartThe thunder of gunsTore me apartYou've beenThunderstruck\\\\n\\\\nRode down the highwayBroke the limit\", ' we hit the townWent through to Texas', ' yeah', ' Texas', ' and we had some funWe met some girlsSome dancers who gave a good timeBroke all the rulesPlayed all the foolsYeah', ' yeah', ' they', ' they', ' they blew our mindsAnd I was shaking at the kneesCould I come again', ' please?Yeah', \" them ladies were too kindYou've beenThunderstruck\", ' thunderstruckYeah', ' yeah', ' yeah', ' thunderstruckOoh', ' thunderstruck', ' yeah\\\\n\\\\nI was shaking at the kneesCould I come again', ' please? Oh\\\\n\\\\nThunderstruck', ' thunderstruckYeah', ' yeah', ' yeah', ' thunderstruck', ' thunderstruckYeah', ' yeah', ' yeah', ' said', ' yeah', \" it's alright\", \" we're doin' fineYeah\", \" it's alright\", \" we're doin' fine\", ' fine', ' fineThunderstruck', ' yeah', ' yeah', ' yeahThunderstruck', ' thunderstruckThunderstruck', ' whoa', ' baby', ' babyThunderstruck', \" you've been thunderstruckThunderstruck\", ' thunderstruckThunderstruck', ' you\\'ve been thunderstruck\"}']\n\nlyrics, thunder, railroad, track, turning back, mind, help, drums, heart, guns, tore, apart, highway, broke, limit, hit town, went through to Texas, fun, met some girls, dancers who gave a good time., broke all the rules.,",
  temperature=0.3,
  max_tokens=60,
  top_p=1,
  frequency_penalty=0.8,
  presence_penalty=0
)

print(response)