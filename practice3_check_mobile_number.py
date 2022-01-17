#10 or 11 or 12 or 13 digit mobile number
import re
number=input("enter mobile number")

if len(number)==10:
    match=re.fullmatch("[7-9]\d{9}",number)
    if match != None:
        print("the number {} is valid".format(number))
    else:
        print("the number {} is not valid".format(number))
elif len(number)==11:
    match=re.fullmatch("[0][6-9]\d{9}",number)
    if match != None:
        print("the number {} is valid".format(number))
    else:
        print("the number {} is not valid".format(number))
elif len(number)==12:
    match=re.fullmatch("[9][1][7-9]\d{9}",number)
    if match != None:
        print("the number {} is valid".format(number))
    else:
        print("the number {} is not valid".format(number))
elif len(number)==13:
    match=re.fullmatch("[+][9][1][7-9]\d{9}",number)
    if match != None:
        print("the number {} is valid".format(number))
    else:
        print("the number {} is not valid".format(number))
else:
    print("please enter valid number")
