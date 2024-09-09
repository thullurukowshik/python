w = input()
length = len(w)
result = w[0]
for i in range(1,length):
    k = w[i]
    upper_char=k.upper()
    
    if k == upper_char:
        k = k.lower()
        result= result + "-" +  k 
    else:
        result = result+ k 
print(result)
