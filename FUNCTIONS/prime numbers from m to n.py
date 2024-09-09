def check_is_prime(m, n):
    
    # complete this 
    store = ""
    for i in range(m,n+1):
        count=0
        for j in range(1,n+1):
            if i%j==0:
                count = count + 1 
        if count == 2 :
            store = store + str(i) + " "
    return store
    
m = int(input())
n = int(input())

prime_numbers =check_is_prime(m,n)

print(prime_numbers)
