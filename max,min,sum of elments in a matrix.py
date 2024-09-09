def convert_string_to_int(list_a):
    new_list = []
    for item in list_a:
        num = int(item)
        new_list.append(num)
    return new_list
    
def max_min_sum(num_list):
    list_a = []
    for each_list in num_list:
        for each_value in each_list:
            list_a.append(each_value)
    print(max(list_a))
    print(min(list_a))
    print(sum(list_a))
        
m, n = input().split()
m, n = int(m), int(n)
num_list = []

for i in range(m):
    list_a = input().split()
    list_a = convert_string_to_int(list_a)
    num_list.append(list_a)

max_min_sum(num_list)
# input has to given in a matrix 
