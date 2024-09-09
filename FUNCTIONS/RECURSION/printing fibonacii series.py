def fibonacci(n):
    # Complete this function to return nth term in fibonacci series
    if n<=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def get_fibonacci_series(n):
    # Complete this function to return list of n terms of fibonacci series
    series = []
    for i in range(n):
        term = fibonacci(i)
        series.append(term)
    return series

n = int(input())
print(get_fibonacci_series(n))
