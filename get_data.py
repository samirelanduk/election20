import json
from time import sleep
import requests

fetched_data = requests.get("https://graphics.thomsonreuters.com/2020-US-elex/20201103/20201103-county.json").json()
states = list(fetched_data["P"].values())

data = {}

lookup = {
    "REP": "Republicans",
    "DEM": "Democrats",
    "LIB": "Libertarians",
    "GRN": "Greens",
    "WRI": "Write-ins"
}


for state in states:
    name = state["0"][0][0]
    if name != "United States":
        data[name] = {
            "name": name,
            "parties": {
                lookup.get(party[2], party[2]): party[4] for party in state["0"][1]
            }
        }
    
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)