def replace_old_value_with_new_value(matrix, old_value, new_value):
    # Complete this function
    for row in matrix:
        for value in row:
            if value == old_value:
                index = row.index(old_value)
                row[index] = new_value
        print(row)
          


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

values = input().split()
old_value, new_value = convert_string_to_int(values)

replace_old_value_with_new_value(num_list,old_value,new_value)
# Write your code here
