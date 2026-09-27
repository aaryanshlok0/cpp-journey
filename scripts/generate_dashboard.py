import json
from pathlib import Path
from datetime import datetime


# -----------------------------------
# Paths
# -----------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

STATS_FILE = BASE_DIR / "stats.json"
SVG_FILE = BASE_DIR / "assets" / "cp-stats.svg"
README_FILE = BASE_DIR / "README.md"


# -----------------------------------
# Load stats
# -----------------------------------

with open(STATS_FILE, "r", encoding="utf-8") as f:
    stats = json.load(f)


rating = stats.get("rating", 0)
max_rating = stats.get("maxRating", 0)
rank = stats.get("rank", "unrated")
contests = stats.get("contests", 0)

rating_history = stats.get("ratingHistory", [])

updated = stats.get("updated", "")

if updated:
    try:
        updated_date = datetime.fromisoformat(
            updated.replace("Z", "+00:00")
        ).strftime("%d %b %Y")
    except Exception:
        updated_date = updated
else:
    updated_date = "Unknown"


# -----------------------------------
# Create rating graph
# -----------------------------------

WIDTH = 900
HEIGHT = 420

GRAPH_LEFT = 70
GRAPH_RIGHT = 850
GRAPH_TOP = 90
GRAPH_BOTTOM = 330

graph_width = GRAPH_RIGHT - GRAPH_LEFT
graph_height = GRAPH_BOTTOM - GRAPH_TOP


ratings = []

for item in rating_history:

    if isinstance(item, dict):

        if "newRating" in item:
            ratings.append(item["newRating"])

        elif "rating" in item:
            ratings.append(item["rating"])


# Prevent empty graph
if not ratings:
    ratings = [rating]


min_rating = min(ratings)
max_graph_rating = max(ratings)

# Add some vertical padding
padding = max(100, int((max_graph_rating - min_rating) * 0.15))

min_graph_rating = min_rating - padding
max_graph_rating += padding


def x_position(index):

    if len(ratings) == 1:
        return GRAPH_LEFT

    return GRAPH_LEFT + (
        index / (len(ratings) - 1)
    ) * graph_width


def y_position(value):

    return GRAPH_BOTTOM - (
        (value - min_graph_rating)
        / (max_graph_rating - min_graph_rating)
    ) * graph_height


points = []

for i, value in enumerate(ratings):

    x = x_position(i)
    y = y_position(value)

    points.append(f"{x:.1f},{y:.1f}")


polyline_points = " ".join(points)


# -----------------------------------
# Generate SVG
# -----------------------------------

svg = f'''<svg width="{WIDTH}" height="{HEIGHT}"
viewBox="0 0 {WIDTH} {HEIGHT}"
xmlns="http://www.w3.org/2000/svg">

<rect width="100%" height="100%" rx="16"
fill="#0d1117"/>

<!-- Title -->

<text x="40" y="45"
font-family="Arial"
font-size="24"
font-weight="bold"
fill="#ffffff">

Codeforces Stats

</text>


<!-- Updated -->

<text x="40" y="70"
font-family="Arial"
font-size="12"
fill="#8b949e">

Updated: {updated_date}

</text>


<!-- Current Rating -->

<text x="760" y="42"
font-family="Arial"
font-size="26"
font-weight="bold"
fill="#58a6ff">

{rating}

</text>

<text x="760" y="62"
font-family="Arial"
font-size="11"
fill="#8b949e">

CURRENT RATING

</text>


<!-- Graph -->

<line
x1="{GRAPH_LEFT}"
y1="{GRAPH_BOTTOM}"
x2="{GRAPH_RIGHT}"
y2="{GRAPH_BOTTOM}"
stroke="#30363d"/>

<line
x1="{GRAPH_LEFT}"
y1="{GRAPH_TOP}"
x2="{GRAPH_LEFT}"
y2="{GRAPH_BOTTOM}"
stroke="#30363d"/>


<!-- Rating graph -->

<polyline
points="{polyline_points}"
fill="none"
stroke="#58a6ff"
stroke-width="3"
stroke-linejoin="round"
stroke-linecap="round"
/>


<!-- Data points -->

'''

for i, value in enumerate(ratings):

    x = x_position(i)
    y = y_position(value)

    svg += f'''
<circle
cx="{x:.1f}"
cy="{y:.1f}"
r="4"
fill="#58a6ff">
<title>Rating: {value}</title>
</circle>
'''


# -----------------------------------
# Bottom statistics
# -----------------------------------

svg += f'''

<!-- Bottom stats -->

<text x="80" y="375"
font-family="Arial"
font-size="15"
fill="#8b949e">

MAX RATING

</text>

<text x="80" y="400"
font-family="Arial"
font-size="22"
font-weight="bold"
fill="#ffffff">

{max_rating}

</text>


<text x="300" y="375"
font-family="Arial"
font-size="15"
fill="#8b949e">

RANK

</text>

<text x="300" y="400"
font-family="Arial"
font-size="22"
font-weight="bold"
fill="#ffffff">

{rank}

</text>


<text x="520" y="375"
font-family="Arial"
font-size="15"
fill="#8b949e">

CONTESTS

</text>

<text x="520" y="400"
font-family="Arial"
font-size="22"
font-weight="bold"
fill="#ffffff">

{contests}

</text>


</svg>
'''


# -----------------------------------
# Save SVG
# -----------------------------------

SVG_FILE.parent.mkdir(
    parents=True,
    exist_ok=True
)

with open(SVG_FILE, "w", encoding="utf-8") as f:
    f.write(svg)


print("Generated:", SVG_FILE)


# ==================================================
# UPDATE README
# ==================================================

README_START = "<!-- CF_STATS_START -->"
README_END = "<!-- CF_STATS_END -->"


new_stats_section = f'''{README_START}

- **Current Rating:** {rating}
- **Maximum Rating:** {max_rating}
- **Rank:** {rank}
- **Contests:** {contests}
- **Rating History:** 📈 {len(ratings)} contests

{README_END}'''


# -----------------------------------
# Read README
# -----------------------------------

with open(README_FILE, "r", encoding="utf-8") as f:
    readme = f.read()


# -----------------------------------
# Replace existing section
# -----------------------------------

if README_START in readme and README_END in readme:

    start = readme.index(README_START)
    end = readme.index(README_END) + len(README_END)

    readme = (
        readme[:start]
        + new_stats_section
        + readme[end:]
    )

else:

    print(
        "WARNING: README markers not found."
    )

    print(
        "Add the CF_STATS_START and CF_STATS_END markers manually."
    )


# -----------------------------------
# Save README
# -----------------------------------

with open(README_FILE, "w", encoding="utf-8") as f:
    f.write(readme)


print("Updated:", README_FILE)

print()
print("Codeforces Stats")
print("----------------")
print("Current Rating:", rating)
print("Maximum Rating:", max_rating)
print("Rank:", rank)
print("Contests:", contests)
print("Rating History:", len(ratings))
