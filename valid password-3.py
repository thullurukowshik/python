w = input()

upper = False
lower = False
digit = False
for i in w:
    if i.isdigit():
        digit = True
    elif i.isupper():
        upper  = True
    elif i.islower():
        lower =True
k = (upper and lower and digit)
if k == True :
    print("Valid Password")
else:
    print("Invalid Password")
    
