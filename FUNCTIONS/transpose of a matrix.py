def get_transpose_of_matrix(matrix, m, n):
    # Complete this function
   for i in range(n):
        individual_list=[]
        for each_list in matrix:
            elements = each_list[i]
            individual_list.append(elements)
        print(individual_list)
    

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

get_transpose_of_matrix(num_list,m,n)
