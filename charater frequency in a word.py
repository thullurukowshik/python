string = input()
string = string.lower()
set_a = set(string)
set_a.discard(' ')
list_a = list(set_a)
list_a.sort()

for i in list_a:
    char_frequency = string.count(i)
    print("{}: {}".format(i,char_frequency))
