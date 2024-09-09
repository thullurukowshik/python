num_list = [(1, 2, 3, 4, 5, 6), (2, 4, 6, 8), (1, 3, 5, 7)]
# Write your code here
n = int(input())
new_list=[]
for each_tuple in num_list:
    for j in each_tuple:
        if n in each_tuple:
            tuple_to_list = list(each_tuple)
            tuple_to_list.remove(n)
            list_to_tuple = tuple(tuple_to_list)
            new_list.append(list_to_tuple)
            break
        else:
            new_list.append(each_tuple)
            break
print(new_list)
