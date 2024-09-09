def get_sum_of_squares(numbers,index=0):
    # Complete this function by calling get_sum_of_squares function
    if len(numbers)==index:
        return 0
    return (int(numbers[index])**2) + get_sum_of_squares(numbers,index+1)

numbers = input().split(" ")

squares_sum = get_sum_of_squares (numbers)
print(squares_sum)
