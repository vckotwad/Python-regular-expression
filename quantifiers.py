import re
match=re.finditer("a","abcdefg")#exactly one a
for m in match:
    print(m.start())
match=re.finditer("a+","abcdefg")#minimum one a
for m in match:
    print(m.start())
match=re.finditer("a*","abcdefg")#all a even 0 a
for m in match:
    print(m.start())
match=re.finditer("a?","abcdefg") #max one a including 0 a
for m in match:
    print(m.start())
match=re.finditer("a{2}","abcdefg")#2 a
for m in match:
    print(m.start())
match=re.finditer("a{2}a*","abcdefg") #min 2 a and all above a
for m in match:
    print(m.start())
match=re.finditer("a{2,3}","abcdefg") #min 2 a and max 3 a
for m in match:
    print(m.start())