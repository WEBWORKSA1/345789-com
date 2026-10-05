import cnlunar, datetime, json, os
os.makedirs('assets/data', exist_ok=True)
from lunardate import LunarDate
# CNY dates
cny={}
for y in range(1900,2101):
    try:
        d=LunarDate(y,1,1).to_solar_date(); cny[y]=d.strftime('%m%d')
    except Exception as e: pass
json.dump(cny,open('assets/data/cny.json','w'),separators=(',',':'))
terms={}; tl=[]
def ix(t):
    if t not in terms: terms[t]=len(tl); tl.append(t)
    return terms[t]
days=[]
d=datetime.date(2026,1,1)
while d<=datetime.date(2028,12,31):
    a=cnlunar.Lunar(datetime.datetime(d.year,d.month,d.day,10,0),godType='8char')
    days.append([a.lunarMonth,a.lunarDay,1 if a.isLunarLeapMonth else 0,a.day8Char,a.chineseZodiacClash,[ix(t) for t in a.goodThing],[ix(t) for t in a.badThing],a.todayLevel,a.todaySolarTerms if a.todaySolarTerms!='无' else ''])
    d+=datetime.timedelta(days=1)
json.dump({'start':'2026-01-01','terms':tl,'days':days},open('assets/data/almanac.json','w'),ensure_ascii=False,separators=(',',':'))
print(len(days),len(tl)); print(tl)
print(days[0])
