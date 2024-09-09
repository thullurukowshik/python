n = list(map(int,input().split()))
new_list = []
maximum_number = max(n)
for i in range(1,maximum_number+1):
    if i not in n:
        new_list+=[i]
print(new_list)
