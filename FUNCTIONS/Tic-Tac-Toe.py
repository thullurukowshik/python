def convert_to_column(list_rows):
    list_cols = []
    for i in range(3):
        list_a = []
        for j in range(3):    
            element = list_rows[j][i]
            list_a.append(element)
        list_cols.append(list_a)
    return list_cols   
def checking_rows(list_rows):
    for i in list_rows:
        if i == ["X", "X", "X"]: 
            return "Anjali Wins - [X X X]"
        elif i == ["O", "O", "O"]:
            return "Abhinav Wins  - [O O O]"
    return checking_cols(list_cols)
def checking_cols(list_cols):
    for i in list_cols:    
        if i == ["O", "O", "O"]: 
            return "Abhinav Wins - [O O O]"
        elif i == ["X", "X", "X"]:
            return "Anjali Wins - [X X X]"
    return checking_diagonals(list_rows)
def checking_diagonals(list_rows):
    list_dia = []
    for i in range(3):
        if list_rows[i][i] == "X" or list_rows[i][i] == "O":
            list_dia.append(list_rows[i][i])
    if list_dia == ["O", "O", "O"]: 
        return "Abhinav Wins - [O O O]"
    elif list_dia == ["X", "X", "X"]:
        return "Anjali Wins - [X X X]"
    return checking_diagonals_1(list_rows)    
def checking_diagonals_1(list_rows):        
    list_dia1 = []
    for i in range(3):
        if list_rows[i][2-i] == "X" or list_rows[i][2-i] == "O":
            list_dia1.append(list_rows[i][2-i])
    if list_dia1 == ["O", "O", "O"]: 
        return "Abhinav Wins - [O O O]"
    elif list_dia1 == ["X", "X", "X"]:
        return "Anjali Wins - [X X X]"
    else:
        return "Tie"
list_rows = []
for i in range(3):
    n = input().split()
    list_rows.append(n)
list_cols=convert_to_column(list_rows)
print(checking_rows(list_rows))










#another method
s = input().split(" ")
t = input().split(" ")
u = input().split(" ")
if (s[0]=="X"and s[1]=="X"and s[2]=="X")or(t[0]=="X"and t[1]== "X"and t[2]== "X")or(u[0]=="X"and u[1]== "X"and u[2]== "X")or(s[0]=="X"and t[1]=="X"and u[2]=="X")or(s[2]=="X"and t[1]=="X"and u[0]=="X")or(s[0]=="X"and t[0]=="X"and u[0]=="X")or(s[1]=="X"and t[1]=="X"and u[1]=="X")or(s[2]=="X"and t[2]=="X"and u[2]=="X"):
    res = "Anjali Wins"
elif(s[0]=="O"and s[1]=="O"and s[2]=="O")or(t[0]=="O"and t[1]== "O"and t[2]== "O")or(u[0]=="O"and u[1]== "O"and u[2]== "O")or(s[0]=="O"and t[1]=="O"and u[2]=="O")or(s[2]=="O"and t[1]=="O"and u[0]=="O")or(s[0]=="O"and t[0]=="O"and u[0]=="O")or(s[1]=="O"and t[1]=="O"and u[1]=="O")or(s[2]=="O"and t[2]=="O"and u[2]=="O"):
    res = "Abhinav Wins"
else:
    res = "Tie"
#print(res)
