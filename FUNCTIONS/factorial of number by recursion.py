def multiply(x):
    if x==1:
        return 1
    return x * multiply(x-1)

n = int(input())
result = multiply(n)
print(result)
