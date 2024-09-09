def get_principal_diagonal_elements(matrix, m, n):
    # Write your code here
    diagonal_list = []
    a=0
    for row in matrix:
        diagonal_list.append(row[a])
        a+=1
    print(diagonal_list)

def convert_string_to_int(list_a):
    new_list = []
    for item in list_a:
        num = int(item)
        new_list.append(num)
    return new_list


m, n = input().split()
m, n = int(m), int(n)
num_list = []

for i in range(m):
    list_a = input().split()
    list_a = convert_string_to_int(list_a)
    num_list.append(list_a)

get_principal_diagonal_elements(num_list,m,n)
