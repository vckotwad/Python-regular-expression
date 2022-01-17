import re
match=re.finditer('\w','abdAjjdE@134* &hdS') #all alphnumeric 
for m in match:
    print(m.start())
match=re.finditer('\w','abdAjjdE@134* &hdS')#except alphanumeric
for m in match:
    print(m.start())
match=re.finditer('\s','abdAjjdE@134* &hdS')#all spaces
for m in match:
    print(m.start())
match=re.finditer('\S','abdAjjdE@134* &hdS')#except spaces
for m in match:
    print(m.start())
match=re.finditer('\d','abdAjjdE@134* &hdS')#all digits
for m in match:
    print(m.start())
match=re.finditer('\D','abdAjjdE@134* &hdS')#except digits
for m in match:
    print(m.start())
match=re.finditer('.','abdAjjdE@134* &hdS') #dot represents everythin
for m in match:
    print(m.start())
match=re.finditer('^a','abdAjjdE@134* &hdS') #starts with 
for m in match:
    print(m.start())
match=re.finditer('s$','abdAjjdE@134* &hdS',re.IGNORECASE) #ends with also we can pass third argument if want to ignore case
for m in match:
    print(m.start())

    