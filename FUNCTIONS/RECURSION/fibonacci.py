def fibonacci(n):
    if n <=  1  :
        return n
    return fibonacci(n-1) + fibonacci(n-2)

list_a = []
n = int(input())
for i in range(n):
    list_a.append(fibonacci(i))
print(list_a)
