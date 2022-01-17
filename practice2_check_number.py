#10 digit mobile number
import re
number=input("enter mobile number")
valid=re.fullmatch("[7-9]\d{9}",number)
if valid != None:
    print("the {} is valid".format(number))
else:
    print("the number is not valid")