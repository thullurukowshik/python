n = int(input())
n = str(n)
count = 0
for i in n:
    if int(i) % 2 == 0:
        count = count + 1
if count > 2:
    print("Count of even digits is greater than two")
else:
    print("Count of even digits is not greater than two")
