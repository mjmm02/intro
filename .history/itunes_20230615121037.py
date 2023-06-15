import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

# response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=coldplay")
response = requests.get("https://itunes.apple.com/search?entity=song&term=" + sys.argv[1])

f = open(sys.ar.json", "w")

resultados = response.json()
# print(response.json())

for result in resultados["results"]:
    print(result["trackName"], end="\n")
# print(json.dumps(response.json(), indent=2))
# coldplay = json.dumps(response.json(), indent=2)
# f.write(str(coldplay))
# f.close()

# f = open("itunes.json","r")
# print(f.read())