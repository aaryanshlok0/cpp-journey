import requests
import json
from datetime import datetime

HANDLE = "aaryanshlok"


# -----------------------------
# Get Codeforces user info
# -----------------------------

info_url = f"https://codeforces.com/api/user.info?handles={HANDLE}"

info = requests.get(info_url).json()

user = info["result"][0]


# -----------------------------
# Get rating history
# -----------------------------

rating_url = f"https://codeforces.com/api/user.rating?handle={HANDLE}"

rating_data = requests.get(rating_url).json()

rating_history = rating_data["result"]


# -----------------------------
# Create stats object
# -----------------------------

stats = {
    "handle": user["handle"],
    "rating": user.get("rating", 0),
    "maxRating": user.get("maxRating", 0),
    "rank": user.get("rank", "unrated"),
    "maxRank": user.get("maxRank", "unrated"),
    "contests": len(rating_history),

    "ratingHistory": [
        {
            "contest": contest["contestName"],
            "rating": contest["newRating"],
            "date": contest["ratingUpdateTimeSeconds"]
        }
        for contest in rating_history
    ],

    "updated": datetime.now().strftime("%d %b %Y")
}


# -----------------------------
# Save stats.json
# -----------------------------

with open("stats.json", "w") as f:
    json.dump(stats, f, indent=4)


print("Stats updated successfully!")
print(f"Handle: {stats['handle']}")
print(f"Rating: {stats['rating']}")
print(f"Max Rating: {stats['maxRating']}")
print(f"Contests: {stats['contests']}")
