n = int(input())
new_list=[]

for i in range(n):
    inputs = list(map(int,input().split()))
    length_list = len(inputs)
    list_to_set = set(inputs)
    length_set = len(list_to_set)
    if length_set==length_list:
        new_list.append(inputs)
print(new_list)
