def is_prime(n):
    # complete this 
    store = ""
    for i in range(1,n+1):
        count=0
        for j in range(1,n+1):
            if i%j==0:
                count = count + 1
        if count == 2:
            store = store + str(i) + " "
    print(store)

n = int(input())
is_prime(n)
