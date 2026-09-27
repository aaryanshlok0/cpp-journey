import json
import os
from datetime import datetime, timedelta


# --------------------------------
# Load stats
# --------------------------------

with open("stats.json", "r", encoding="utf-8") as f:
    stats = json.load(f)


submissions = stats.get("submissions", [])


# --------------------------------
# Count submissions per day
# --------------------------------

activity = {}

for submission in submissions:

    date = datetime.fromtimestamp(
        submission["date"]
    ).strftime("%Y-%m-%d")

    activity[date] = activity.get(date, 0) + 1


# --------------------------------
# Last 365 days
# --------------------------------

today = datetime.now().date()

start_date = today - timedelta(days=364)


# --------------------------------
# SVG dimensions
# --------------------------------

cell_size = 12
gap = 3

width = 850
height = 170

left = 40
top = 35


# --------------------------------
# SVG
# --------------------------------

svg = f'''<svg
xmlns="http://www.w3.org/2000/svg"
width="{width}"
height="{height}"
viewBox="0 0 {width} {height}">

<rect
width="100%"
height="100%"
rx="12"
fill="#0d1117"/>


<text
x="20"
y="25"
fill="#ffffff"
font-size="15"
font-family="Arial"
font-weight="bold">

Codeforces Activity

</text>
'''


# --------------------------------
# Generate cells
# --------------------------------

current = start_date

while current <= today:

    day_number = (
        current - start_date
    ).days

    week = day_number // 7
    day = current.weekday()

    x = (
        left
        + week * (cell_size + gap)
    )

    y = (
        top
        + day * (cell_size + gap)
    )

    date_string = current.strftime(
        "%Y-%m-%d"
    )

    count = activity.get(
        date_string,
        0
    )


    # --------------------------------
    # Intensity
    # --------------------------------

    if count == 0:
        fill = "#161b22"

    elif count == 1:
        fill = "#0e4429"

    elif count <= 3:
        fill = "#006d32"

    elif count <= 6:
        fill = "#26a641"

    else:
        fill = "#39d353"


    svg += f'''
<rect
x="{x}"
y="{y}"
width="{cell_size}"
height="{cell_size}"
rx="2"
fill="{fill}">

<title>
{date_string}: {count} submissions
</title>

</rect>
'''


    current += timedelta(days=1)


# --------------------------------
# Legend
# --------------------------------

legend_y = 140

svg += f'''

<text
x="610"
y="{legend_y}"
fill="#8b949e"
font-size="11"
font-family="Arial">

Less

</text>

<rect
x="645"
y="{legend_y - 10}"
width="12"
height="12"
rx="2"
fill="#161b22"/>

<rect
x="662"
y="{legend_y - 10}"
width="12"
height="12"
rx="2"
fill="#0e4429"/>

<rect
x="679"
y="{legend_y - 10}"
width="12"
height="12"
rx="2"
fill="#006d32"/>

<rect
x="696"
y="{legend_y - 10}"
width="12"
height="12"
rx="2"
fill="#26a641"/>

<rect
x="713"
y="{legend_y - 10}"
width="12"
height="12"
rx="2"
fill="#39d353"/>

<text
x="733"
y="{legend_y}"
fill="#8b949e"
font-size="11"
font-family="Arial">

More

</text>

</svg>
'''


# --------------------------------
# Save
# --------------------------------

os.makedirs(
    "assets",
    exist_ok=True
)

with open(
    "assets/cp-heatmap.svg",
    "w",
    encoding="utf-8"
) as f:

    f.write(svg)


print(
    "Codeforces heatmap generated!"
)
