num_list = [(2, 4, 6, 8), (5, 15, 25, 35), (7, 14, 21)]
# Write your code here
n = int(input())
for i in range(len(num_list)):
    for j in range(len(num_list[i])):
        if n == num_list[i][j]:
            print("{} {}".format(i,j))
