num_list = [(10, 20, 30), (1, 2), (5, 10, 15, 45)]
# Write your code here
n = int(input())
new_list = []
for i in num_list:
    tuple_a = i[:-1] + (n,)
    new_list.append(tuple_a)
print(new_list)
