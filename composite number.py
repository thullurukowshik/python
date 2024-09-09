n = int(input())
factors = 0
for i in range(1,n+1):
    if n%i==0:
        factors = factors + 1  
if factors > 2:
    print("True")
else:
    print("False")


    #if a number is having greater than two factors it is called composite number.
