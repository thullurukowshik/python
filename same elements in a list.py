n = list(map(int,input().split()))
k = n[0]
length = len(n)
set_a=set()
count = 0
for i in n:
    if i == k:
        count+=1
    else:
        set_a.update((i,k))
set_a_list = list(set_a)
if count==length:
    print("True")
else:
    print(sorted(set_a_list))
    
