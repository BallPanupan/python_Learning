#ค้นหาสตริงเพื่อดูว่าขึ้นต้นด้วย "The" และลงท้ายด้วย "Spain" หรือไม่:

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")
