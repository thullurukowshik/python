n = input().split()
new_list = []
for i in n:
    new_list+=[int(i)]
set_a = set(new_list)
dup_list = list(set_a)
print(sorted(dup_list))
