#match is used if string start with the pattern
import re
s='abc'
string='abcdefg'
m=re.match(s,string)
if m!=None:
    print(m.start(), m.end())
else:
    print("match not foound")