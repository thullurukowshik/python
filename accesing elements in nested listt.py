list_a = [('apple', 'banana', 'orange', 'grapes'), ('cricket', 'football', 'hockey'), ('car', 'bicycle', 'bus')]
# Write your code here
n = int(input())
new_list = []
for i in range(n):
    a,b=map(int,input().split())
    for i in list_a:
        index = list_a[a][b]
        new_list.append(index)
        break
print(new_list)    
