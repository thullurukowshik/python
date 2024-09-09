def print_max_min_sum_for_row_wise(num_list):
    # Complete this function
    maximum_list=[]
    minimum_list=[]
    sum_list=[]
    for each_list in num_list:
        maximum,minimum,sum_row = max(each_list),min(each_list),sum(each_list)
        maximum_list.append(maximum)
        minimum_list.append(minimum)
        sum_list.append(sum_row)
    print(maximum_list)
    print(minimum_list)
    print(sum_list)

def convert_string_to_int(list_a):
    new_list = []
    for item in list_a:
        num = int(item)
        new_list.append(num)
    return new_list


m, n = input().split()
m, n = int(m), int(n)
num_list = []

for i in range(m):
    list_a = input().split()
    list_a = convert_string_to_int(list_a)
    num_list.append(list_a)

print_max_min_sum_for_row_wise(num_list)
