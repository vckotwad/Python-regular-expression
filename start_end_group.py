import re
pattern="ab"
string="abcdabef"
match=re.finditer(pattern,string)# returns iterator object
for m in match:
    print(m.start(),m.end(),m.group())