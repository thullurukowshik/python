s = input()

length = len(s)

sum = ""

for i in range(1,length+1):

    char = length - i

    reverse = s[char]
    
    sum = sum + reverse

print(sum)

