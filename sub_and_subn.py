import re
new=re.sub('\d','#','1gf3d3jfd') #replace the pattern with new string you want
print(new)
number=re.subn('\d','#','1gf3d3jfd') 
print(number) #return no of times the replacement happened #return type is a tuple(string,number_of_replacement)
print(number[0])
print(number[1])