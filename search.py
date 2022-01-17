#search is used if pattern in the string and return only first occurence
import re
pattern='aa'
string='baacaadaa'
m=re.search(pattern,string)
if m != None:
    print("index is",m.start())
else:
    print("not found")