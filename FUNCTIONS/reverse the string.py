def str_reverse(str1):
    if (len(str1) == 0 or len(str1) == 1):
        return str1
    else:
        return str1[len(str1)-1] + str_reverse(str1[:len(str1)-1])

str1 = input()
print(str_reverse(str1))
