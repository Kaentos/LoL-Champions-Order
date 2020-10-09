import requests
import json
import pathlib

current_path = pathlib.Path(__file__).parent.absolute()
destination_path = f"{current_path}/ordered_champions.json"

def request_json(url):
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    else:
        print("Error: " + r.status_code)
        exit()

version = request_json("https://ddragon.leagueoflegends.com/api/versions.json")[0]
data = request_json(f"http://ddragon.leagueoflegends.com/cdn/{version}/data/en_US/champion.json")

final = {}
for champion, data in data["data"].items():
    final[data["key"]] = data
    
with open(destination_path, "w") as final_file:
    json.dump(final, final_file, indent=4)