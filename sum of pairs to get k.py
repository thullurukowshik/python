n = list(map(int,input().split(",")))
k = int(input())
print(n)
set_a=set()
a = 0
for i in n:
    a=a+1
    for j in n[a:]:
        if i+j == k:
            pair_tuple = (i,j)
            pair_list = list(pair_tuple)
            sort_pair = sorted(pair_list)
            sort_tuple = tuple(sort_pair)
            set_a.add(sort_tuple)

set_list = list(set_a)
set_list.sort()
for i in set_list:
    print(i)

#another method
n = list(map(int,input().split(",")))
k = int(input())
set_a = set()
stop_index = len(n)-1
for i in range(stop_index):
    num_1 = n[i]
    num_2 = k - num_1
    remaining_list = n[i+1:]
    if num_2 in remaining_list:
        pair = (num_1,num_2)
        sorted_tuple = tuple(sorted(pair))
        set_a.add(sorted_tuple)
set_list = list(set_a)
set_list.sort()
#for i in set_list:
    #print(i)
