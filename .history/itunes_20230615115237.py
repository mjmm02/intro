import json
import requests
import sys

if len(sys.argv) != 1:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=coldplay")

f = open("itunes.txt", "w")

#print(response.json())
#print(json.dumps(response.json(), indent=2))
coldplay = json.dumps(response.json(), indent=2)
f.write(str(coldplay))
f.close()

f = open("coldplay.txt","r")
print(f.read())