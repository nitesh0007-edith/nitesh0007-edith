"""Render genuine GitHub contribution data as a Tokyo Night SVG. Requires gh auth."""

import json
import subprocess
import sys
from datetime import datetime, timezone
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUERY = """query {
  user(login: "nitesh0007-edith") {
    contributionsCollection {
      contributionCalendar {
        totalContributions
        weeks { contributionDays { contributionCount contributionLevel date weekday } }
      }
    }
  }
}"""
COLORS = {
    "NONE": "#1D243B",
    "FIRST_QUARTILE": "#293D68",
    "SECOND_QUARTILE": "#4566AA",
    "THIRD_QUARTILE": "#7AA2F7",
    "FOURTH_QUARTILE": "#BB9AF7",
}


def main():
    result = subprocess.run(
        ["gh", "api", "graphql", "-f", f"query={QUERY}"],
        check=True, capture_output=True, text=True,
    )
    payload = json.loads(result.stdout)
    if payload.get("errors"):
        raise RuntimeError("GitHub did not return contribution data")
    calendar = payload["data"]["user"]["contributionsCollection"]["contributionCalendar"]
    weeks = calendar["weeks"]
    days = [day for week in weeks for day in week["contributionDays"]]
    assert days and sum(day["contributionCount"] for day in days) == calendar["totalContributions"]
    updated = datetime.now(timezone.utc).strftime("%d %b %Y")
    total = calendar["totalContributions"]
    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="300" viewBox="0 0 1200 300" role="img" aria-labelledby="activity-title activity-desc">',
        '<title id="activity-title">Nitesh Ranjan Singh — GitHub contribution heatmap</title>',
        f'<desc id="activity-desc">{total} contributions from {days[0]["date"]} to {days[-1]["date"]}. Genuine GitHub API data, updated {updated} UTC. Each square represents one day.</desc>',
        '<rect width="1200" height="300" rx="16" fill="#0B1020"/>',
        '<g font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Arial, sans-serif">',
        '<text x="40" y="42" fill="#7AA2F7" font-size="13" letter-spacing="3">CONSISTENCY / CONTRIBUTION LOG</text>',
        f'<text x="40" y="76" fill="#E0E7FF" font-size="23">{total:,} contributions</text>',
        f'<text x="1160" y="75" text-anchor="end" fill="#7AA2F7" font-size="13">{days[0]["date"]} — {days[-1]["date"]}</text>',
    ]
    previous_month = None
    for column, week in enumerate(weeks):
        first = week["contributionDays"][0]
        month = first["date"][:7]
        x = 78 + column * 20
        if month != previous_month:
            label = datetime.strptime(first["date"], "%Y-%m-%d").strftime("%b")
            parts.append(f'<text x="{x}" y="108" fill="#7AA2F7" font-size="11">{label}</text>')
            previous_month = month
        for day in week["contributionDays"]:
            y = 120 + day["weekday"] * 17
            color = COLORS[day["contributionLevel"]]
            label = escape(f'{day["date"]}: {day["contributionCount"]} contributions')
            parts.append(f'<rect x="{x}" y="{y}" width="15" height="13" rx="3" fill="{color}"><title>{label}</title></rect>')
    for label, row in [("Mon", 1), ("Wed", 3), ("Fri", 5)]:
        parts.append(f'<text x="40" y="{130 + row * 17}" fill="#7AA2F7" font-size="11">{label}</text>')
    parts.append(f'<text x="40" y="275" fill="#7AA2F7" font-size="12">Source: GitHub contribution calendar · Updated {updated} UTC</text>')
    parts.append('<text x="966" y="275" fill="#7AA2F7" font-size="11">Less</text>')
    for index, color in enumerate(COLORS.values()):
        parts.append(f'<rect x="{1000 + index * 20}" y="264" width="15" height="13" rx="3" fill="{color}"/>')
    parts.append('<text x="1107" y="275" fill="#7AA2F7" font-size="11">More</text></g></svg>')
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "assets" / "activity.svg"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("\n".join(parts) + "\n")
    print(f"Updated {target.name}: {total} genuine contributions, {len(days)} days")


if __name__ == "__main__":
    main()
