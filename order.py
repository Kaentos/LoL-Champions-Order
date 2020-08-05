import json
import pathlib

current_path = pathlib.Path(__file__).parent.absolute()

with open(f"{current_path}/champion.json", encoding="utf8") as json_file:
    data = json.load(json_file)

final = {}
for champion, data in data["data"].items():
    final[data["key"]] = {
        "name": data["name"],
        "nameID": data["id"],
        "title": data["title"],
        "image": data["image"]["full"]
    }

with open(f"{current_path}/ordered_champions.json", "w") as final_file:
    json.dump(final, final_file, indent=4)