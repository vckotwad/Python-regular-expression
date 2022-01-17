#full match used when pattern fully matched with string
import re
pattern="abcdefg"
string="abcdefg"
m=re.fullmatch(pattern,string)
if m!=None:
    print("full match")
else:
    print("not matched")