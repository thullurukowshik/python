m = input().split(",")
n = int(input())
new= []
for i in m:
    new= new +[int(i)]
sort = sorted(new)
sum_numbers = sort[:(n)]
print(sum(sum_numbers))
