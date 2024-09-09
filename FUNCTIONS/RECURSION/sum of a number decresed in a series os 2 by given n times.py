def get_sum_of_series(x,y,var=0,sum=0):
    # Complete this recursive function
    if y == 0:
        return 0
    return sum + (x - var) + get_sum_of_series(x,y-1,var+2)



number = int(input())
number_of_terms = int(input())

series_sum =get_sum_of_series(number,number_of_terms)
print(series_sum)
