n = int(input())

k = len(str(n))

sum=0

for i in range(1,k+1):

    power = i ** k

    sum = sum + power

print(sum)
    
