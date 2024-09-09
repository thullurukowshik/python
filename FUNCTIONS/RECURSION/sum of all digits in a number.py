def sum_of_the_digits(n,index=0,sum=0):
    # Complete this recursive function
    if len(n) == index:
        return 0
    return sum + n[index] + sum_of_the_digits(n,index+1)


number = str(int(input()))
list = []
for i in number:
    list = list + [int(i)]
print(sum_of_the_digits (list))
