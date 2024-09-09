n = int(input())
hollow_spaces_count=-1

spaces = n-1
left_spaces = " " * spaces
print(left_spaces+"*")

for i in range(2,n+1):
    spaces = n-i
    left_spaces=" " * spaces
    hollow_spaces_count = hollow_spaces_count + 2
    hollow_spaces = " " * hollow_spaces_count 
    print(left_spaces+"*"+hollow_spaces+"*")
    
for i in range(1,n-1):
    spaces = i
    left_spaces=" " * spaces
    hollow_spaces_count = hollow_spaces_count - 2
    hollow_spaces = " " * hollow_spaces_count 
    print(left_spaces+"*"+hollow_spaces+"*")

spaces = n-1
left_spaces = " " * spaces
print(left_spaces+"*")





    
