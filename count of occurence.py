n = input().split()
new_list=[]
for i in n:
    new_list+=[int(i)]
odd_occurence=[]
for i in new_list:
    if i not in odd_occurence:
        count=new_list.count(i)
        if count%2!=0:
            odd_occurence.append(i)
print(sorted(odd_occurence))
