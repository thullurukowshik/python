n = input().split(",")
large_occurence = 0

for i in n:
    if n.count(i) > large_occurence:
        large_occurence = n.count(i)
        mode = i 
print(mode)
