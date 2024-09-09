list_a = [5, 4, 10, 2, 3, 2, 5, 15, 4, 4]
# write your code here
n = int(input())
indices = []

for i in range(len(list_a)):
    if n == list_a[i]:
        indices.append(str(i))
print(" ".join(indices)) 
