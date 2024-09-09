def is_prime(number):
    # complete this function
    count = 0
    for i in range(1,number+1):
        if number%i==0:
            count = count + 1 
    if count == 2:
        return "Prime Number"
    else:
        return "Not a Prime Number"

number = int(input())
result = is_prime(number)
print(result)
