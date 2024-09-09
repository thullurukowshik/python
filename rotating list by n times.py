n = list(map(int,input().split(",")))
k = int(input())

for i in range(k):
    n = n[1:] + [n[0]]
print(n)


#another method
num_list = list(map(int,input().split(",")))
rotating_times = int(input())
length = len(num_list)
rotation = rotating_times % length

first_part = num_list[:(rotation)]
second_part = num_list[rotation:]
new_list = second_part+first_part 
print(new_list)
