n = input().split(",")
new = []
count = 0
for i in n:
    count = count + 1 
    new=new+[int(i)]
sort = sorted(new)
index=((count//2))
if count%2==0:
    median = (sort[index]+sort[index-1])/2
else:
    median = sort[index]
print(median)
