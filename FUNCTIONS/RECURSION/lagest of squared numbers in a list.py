def get_largest_square(numbers,index=0,result = []):
    # Complete this function
    if len(numbers) == index:
        return result
    return result + [int(numbers[index])**2] + get_largest_square(numbers,index+1)

numbers = input().split(" ")

result = get_largest_square (numbers)
print(max(result))
