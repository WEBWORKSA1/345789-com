"""Generate assets/data/cny.json — Lunar New Year dates 1900-2100 (used by the zodiac & Kua tools).
Run: pip install lunardate && python3 gen_data.py
The Lucky Date Finder computes the Chinese Almanac in the browser with lunar-javascript (MIT)."""
import json, os
from lunardate import LunarDate

os.makedirs("assets/data", exist_ok=True)
cny = {}
for y in range(1900, 2101):
    try:
        cny[y] = LunarDate(y, 1, 1).to_solar_date().strftime("%m%d")
    except Exception:
        pass
json.dump(cny, open("assets/data/cny.json", "w"), separators=(",", ":"))
print(len(cny), "years")
