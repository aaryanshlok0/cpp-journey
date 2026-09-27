import requests
import json
from datetime import datetime


HANDLE = "aaryanshlok"


def get_json(url):
    response = requests.get(url, timeout=20)
    response.raise_for_status()

    data = response.json()

    if data["status"] != "OK":
        raise Exception("Codeforces API request failed")

    return data["result"]


# -----------------------------------
# User information
# -----------------------------------

user = get_json(
    f"https://codeforces.com/api/user.info?handles={HANDLE}"
)[0]


# -----------------------------------
# Rating history
# -----------------------------------

rating_history = get_json(
    f"https://codeforces.com/api/user.rating?handle={HANDLE}"
)


# -----------------------------------
# Recent submissions
# -----------------------------------

submissions = get_json(
    f"https://codeforces.com/api/user.status?handle={HANDLE}&from=1&count=1000"
)


# -----------------------------------
# Count accepted problems
# -----------------------------------

accepted = set()

for submission in submissions:

    if submission["verdict"] == "OK":

        problem = submission["problem"]

        key = (
            problem.get("contestId"),
            problem.get("index")
        )

        accepted.add(key)


# -----------------------------------
# Recent contests
# -----------------------------------

recent_contests = []

for contest in rating_history[-5:]:

    recent_contests.append({
        "name": contest["contestName"],
        "oldRating": contest["oldRating"],
        "newRating": contest["newRating"],
        "change": (
            contest["newRating"]
            -
            contest["oldRating"]
        )
    })


# -----------------------------------
# Create stats
# -----------------------------------

stats = {

    "handle": user["handle"],

    "rating": user.get(
        "rating",
        0
    ),

    "maxRating": user.get(
        "maxRating",
        0
    ),

    "rank": user.get(
        "rank",
        "unrated"
    ),

    "maxRank": user.get(
        "maxRank",
        "unrated"
    ),

    "contests": len(
        rating_history
    ),

    "solved": len(
        accepted
    ),

    "ratingHistory": [

        {
            "contest": contest["contestName"],

            "rating": contest["newRating"],

            "change": (
                contest["newRating"]
                -
                contest["oldRating"]
            ),

            "date": contest[
                "ratingUpdateTimeSeconds"
            ]

        }

        for contest in rating_history
    ],

    "recentContests":
        recent_contests,

    "submissions": [

        {
            "date": submission[
                "creationTimeSeconds"
            ],

            "verdict": submission[
                "verdict"
            ]

        }

        for submission in submissions

    ],

    "updated":
        datetime.now().strftime(
            "%d %b %Y • %H:%M"
        )
}


# -----------------------------------
# Save stats.json
# -----------------------------------

with open(
    "stats.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        stats,
        f,
        indent=4
    )


# -----------------------------------
# Console output
# -----------------------------------

print("================================")
print("       CP STATS UPDATED")
print("================================")

print(f"Handle       : {stats['handle']}")
print(f"Rating       : {stats['rating']}")
print(f"Max Rating   : {stats['maxRating']}")
print(f"Rank         : {stats['rank']}")
print(f"Contests     : {stats['contests']}")
print(f"Solved       : {stats['solved']}")
print(f"Submissions  : {len(submissions)}")
print(f"Updated      : {stats['updated']}")

print("================================")
