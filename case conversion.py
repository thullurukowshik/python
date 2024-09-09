word = input()
length = len(word)
result = word[0]
for i in range(1,length):
    k = word[i]
    upper_char= k.upper()
    
    if k == upper_char :
        result = result + " " + k
        
    else:
        result = result + k
        
print(result)
