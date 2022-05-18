import re
string = "Luke Skywarker 02-123-4567 luke@daum.net like, likelihood, likely" 
m1 = re.findall('\w', string)
r1 = re.findall('[a-zA-Z0-9]', string)
r2 = re.findall('[(likeli.* | like.*)]', string)
m2 = re.findall('\w+', string)
print(f"m1 : {m1}\n")
print(f"r1 : {r1}\n")
print(f"r2 : {r2}\n")
print(f"m2 : {m2}\n")

p = re.compile(r"(\w+)\s+(\d+[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group(1))
print(m.group(2))

