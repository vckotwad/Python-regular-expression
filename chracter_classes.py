import re
match=re.finditer("[abc]","abcdefg") #a or b or c
for m in match:
    print(m.start())
match=re.finditer("[^abc]","abcdefg")#except a and b and c
for m in match:
    print(m.start())
match=re.finditer("[a-z]","abcdefg") #from a-z
for m in match:
    print(m.start())
match=re.finditer("[a-zA-Z]","abcdefg")#all small and capital letter
for m in match:
    print(m.start())
match=re.finditer("[0-9]","abcdefg")#all digits
for m in match:
    print(m.start())