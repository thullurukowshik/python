def get_series_sum(n,series=1):
    # Complete this recursive function
    if n == 0:
        return 0
    return 1/series + get_series_sum(n-1,series+1)


number = int(input())

series_sum =get_series_sum (number)

print(round(series_sum,2))

