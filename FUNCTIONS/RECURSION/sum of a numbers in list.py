def get_sum(numbers,index=0):
    # Complete this recursive function
    
    if len(numbers) == index:
        return 0
    return int(numbers[index])+get_sum(numbers,index+1)
    



numbers = input().split(" ")

sum_of_numbers = get_sum(numbers)
print(sum_of_numbers)
