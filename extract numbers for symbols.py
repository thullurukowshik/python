n= input().split(",")
new_list = []
for i in n:
    if i.isdigit():
        new_list=new_list+[int(i)]
print(new_list)
