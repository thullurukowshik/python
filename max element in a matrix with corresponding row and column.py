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
# Write your code here








#method two



def convert_string_to_int(list_a):
    new_list = []
    for item in list_a:
        num = int(item)
        new_list.append(num)
    return new_list

def max_element(num_list):
    list_a = []
    for i in num_list:
        for j in i:
            list_a.append(j)
    max_num = max(list_a)
    #corresponding row having maximum number
    for each_list in num_list:
        if max_num in each_list:
            print(each_list)
            break
    #corresponding column
    list_column = []
    for i in range(n):
        list_col=[]
        for each_list in num_list:
            k = each_list[i]
            list_col.append(k)
        list_column.append(list_col)
    for each_list in list_column:
        if max_num in each_list:
            print(each_list)
            break
        
m, n = input().split()
m, n = int(m), int(n)
num_list = []

for i in range(m):
    list_a = input().split()
    list_a = convert_string_to_int(list_a)
    num_list.append(list_a)

# Write your code here
max_element(num_list)
