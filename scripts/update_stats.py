import requests
import json

HANDLE = "aaryanshlok"

info_url = f"https://codeforces.com/api/user.info?handles={HANDLE}"
rating_url = f"https://codeforces.com/api/user.rating?handle={HANDLE}"

info = requests.get(info_url).json()
rating = requests.get(rating_url).json()

user = info["result"][0]

stats = {
    "handle": user["handle"],
    "rating": user.get("rating", 0),
    "maxRating": user.get("maxRating", 0),
    "rank": user.get("rank", "unrated"),
    "maxRank": user.get("maxRank", "unrated"),
    "contests": len(rating["result"])
}

with open("stats.json", "w") as f:
    json.dump(stats, f, indent=4)

print(stats)
