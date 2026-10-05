"""Generate assets/data/cny.json (Lunar New Year dates 1900-2100) and assets/data/almanac.json
(Chinese Almanac / Tong Shu, 2026-01-01 .. 2028-12-31) in a compact encoding.
Run: pip install cnlunar lunardate && python3 gen_data.py

almanac.json = {"start": "2026-01-01", "terms": [...], "st": {dayIndex: solarTerm}, "d": "<days>"}
Days are separated by "#". Each day = month, day, leap, level, good-term codes... "!" bad-term codes,
every value encoded as one character of ALPHABET (chr 40..125 without backslash).
Day pillar and clash animal are derived in the browser from the 60-day cycle."""
import cnlunar, datetime, json, os
from lunardate import LunarDate

os.makedirs("assets/data", exist_ok=True)
ALPHABET = "".join(chr(c) for c in range(40, 126) if c != 92)

cny = {}
for y in range(1900, 2101):
    try:
        cny[y] = LunarDate(y, 1, 1).to_solar_date().strftime("%m%d")
    except Exception:
        pass
json.dump(cny, open("assets/data/cny.json", "w"), separators=(",", ":"))

terms, tl, days, st = {}, [], [], {}
def ix(t):
    if t not in terms:
        terms[t] = len(tl); tl.append(t)
    return ALPHABET[terms[t]]

d, i = datetime.date(2026, 1, 1), 0
while d <= datetime.date(2028, 12, 31):
    a = cnlunar.Lunar(datetime.datetime(d.year, d.month, d.day, 10, 0), godType="8char")
    if i == 0:
        assert a.day8Char == "乙亥", "cycle anchor changed"
    head = ALPHABET[a.lunarMonth] + ALPHABET[a.lunarDay] + ("1" if a.isLunarLeapMonth else "0") + ALPHABET[a.todayLevel + 1]
    days.append(head + "".join(ix(t) for t in a.goodThing) + "!" + "".join(ix(t) for t in a.badThing))
    if a.todaySolarTerms and a.todaySolarTerms != "无":
        st[i] = a.todaySolarTerms
    d += datetime.timedelta(days=1); i += 1

json.dump({"start": "2026-01-01", "anchor": 11, "terms": tl, "st": st, "d": "#".join(days)},
          open("assets/data/almanac.json", "w"), ensure_ascii=False, separators=(",", ":"))
print(len(days), "days,", len(tl), "terms")
