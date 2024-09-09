#[1,2,3,5,10,11,15,20,30]
def converting_to_matrix(new_list):
    for i in range(m):
        for j in range(n):
            print(str(new_list[0]) + " ",end = '')
            new_list.remove(new_list[0])
        print()
m , n = input().split()
m , n  = int(m) , int(n)
new_list = []
for i in range(m):
    input_1 = list(map(int,input().split()))
    for j in input_1:
        new_list.append(j)
new_list.sort()
converting_to_matrix(new_list)
