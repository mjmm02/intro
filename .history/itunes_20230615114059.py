import json
import requests
import sys

if len(sys.argv) != 1:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=coldplay")
f = open("coldplay.json", "a")
f.write(repsonse)
#print(response.json())
print(json.dumps(response.json(), indent=2))