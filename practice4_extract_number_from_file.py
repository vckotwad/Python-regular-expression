import re
f1=open("input.txt",'r')

f2=open('output.txt','w')
for line in f1:
    
    match=re.findall("[6-9]\d{9}",line)
    if match!= None:
        for number in match:
            f2.write(number)
            f2.write("\n")


f1.close()
f2.close()
    
    