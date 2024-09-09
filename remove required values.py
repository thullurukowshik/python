num_set = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100}
# Write your code here
n = list(map(int,input().split()))
new_set=set(n)
new_list=[]
for i in num_set:
    if i in new_set:
        continue
    else:
        new_list = new_list +[i]
print(sorted(new_list))
    

