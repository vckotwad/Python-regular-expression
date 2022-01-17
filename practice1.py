import re
string=input("enter your string")
m=re.fullmatch('[a-k][0369][a-zA-Z0-9#]*',string)
if m!= None:
    print("this is valid")
else:
    print("this is not valid")