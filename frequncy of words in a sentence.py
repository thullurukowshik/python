n = input().split()
dict_a = dict()

for i in n:
    if i not in dict_a:
        dict_a[i]=1 
    else:
        dict_a[i]+=1 
for key,value in dict_a.items():
    print("{}: {}".format(key,value))
