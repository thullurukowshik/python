list_a=input().split()
list_b=input().split()
m = len(list_a)
k = []
for i in range(m):
    k = k + [list_a[i]] + [list_b[i]]
print(k)
