import json, re
from pathlib import Path
t = Path(r"C:\Users\fassb\Projects\analisis-bodas\index.html").read_text(encoding="utf-8")
m = re.search(r"const venues = (\[.*?\]);", t)
venues = json.loads(m.group(1))
for v in venues:
    print(f"{v['id']}|{v['name']}|{v['place']}|{v.get('vegan','')}|{v.get('rating','')}|{v.get('reviews',0)}|{v.get('from')}-{v.get('to')}|{v.get('bodas','')[:70]}")
print("TOTAL", len(venues))
