import json
import os


# -----------------------------
# Load stats
# -----------------------------

with open("stats.json", "r") as f:
    stats = json.load(f)


handle = stats["handle"]
rating = stats["rating"]
max_rating = stats["maxRating"]
rank = stats["rank"]
contests = stats["contests"]
history = stats["ratingHistory"]
updated = stats["updated"]


# -----------------------------
# Rating graph
# -----------------------------

graph_x = 80
graph_y = 330

graph_width = 700
graph_height = 160

if history:

    ratings = [x["rating"] for x in history]

    min_rating = min(ratings)
    max_graph_rating = max(ratings)

    padding = 100

    min_rating -= padding
    max_graph_rating += padding

    points = []

    for i, r in enumerate(ratings):

        if len(ratings) == 1:
            x = graph_x
        else:
            x = graph_x + (
                i / (len(ratings) - 1)
            ) * graph_width

        y = graph_y + graph_height - (
            (r - min_rating)
            / (max_graph_rating - min_rating)
        ) * graph_height

        points.append(f"{x:.1f},{y:.1f}")

    graph_points = " ".join(points)

else:

    graph_points = ""


# -----------------------------
# Create SVG
# -----------------------------

svg = f'''<svg width="850" height="600"
xmlns="http://www.w3.org/2000/svg">

<rect width="850" height="600"
rx="20"
fill="#0d1117"/>

<!-- Title -->

<text x="50" y="65"
fill="#ffffff"
font-size="30"
font-family="Arial"
font-weight="bold">

⚡ {handle}'s CP Journey

</text>


<!-- Subtitle -->

<text x="50" y="95"
fill="#8b949e"
font-size="15"
font-family="Arial">

Competitive Programming Dashboard

</text>


<!-- Rating card -->

<rect x="50" y="130"
width="220"
height="120"
rx="15"
fill="#161b22"
stroke="#30363d"/>

<text x="70" y="165"
fill="#8b949e"
font-size="14"
font-family="Arial">

CURRENT RATING

</text>

<text x="70" y="210"
fill="#ffffff"
font-size="36"
font-family="Arial"
font-weight="bold">

{rating}

</text>


<!-- Max rating card -->

<rect x="290" y="130"
width="220"
height="120"
rx="15"
fill="#161b22"
stroke="#30363d"/>

<text x="310" y="165"
fill="#8b949e"
font-size="14"
font-family="Arial">

MAX RATING

</text>

<text x="310" y="210"
fill="#ffffff"
font-size="36"
font-family="Arial"
font-weight="bold">

{max_rating}

</text>


<!-- Contests card -->

<rect x="530" y="130"
width="220"
height="120"
rx="15"
fill="#161b22"
stroke="#30363d"/>

<text x="550" y="165"
fill="#8b949e"
font-size="14"
font-family="Arial">

CONTESTS

</text>

<text x="550" y="210"
fill="#ffffff"
font-size="36"
font-family="Arial"
font-weight="bold">

{contests}

</text>


<!-- Rating history -->

<text x="50" y="290"
fill="#ffffff"
font-size="20"
font-family="Arial"
font-weight="bold">

Rating History

</text>


<!-- Graph -->

<line x1="80" y1="490"
x2="780" y2="490"
stroke="#30363d"/>

<line x1="80" y1="330"
x2="80" y2="490"
stroke="#30363d"/>


<polyline
points="{graph_points}"
fill="none"
stroke="#58a6ff"
stroke-width="4"
stroke-linejoin="round"
stroke-linecap="round"/>


<!-- Rank -->

<text x="50" y="540"
fill="#8b949e"
font-size="15"
font-family="Arial">

Rank: {rank}

</text>


<!-- Updated -->

<text x="650" y="540"
fill="#8b949e"
font-size="13"
font-family="Arial">

Updated: {updated}

</text>

</svg>
'''


# -----------------------------
# Save SVG
# -----------------------------

os.makedirs("assets", exist_ok=True)

with open("assets/cp-stats.svg", "w", encoding="utf-8") as f:
    f.write(svg)


print("Dashboard generated successfully!")
