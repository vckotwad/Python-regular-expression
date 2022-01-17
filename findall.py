#find all finds all the pattern and return a string
import re
pattern="aa"
string="baacaadaaeaa"
m=re.findall(pattern,string)
print(m)