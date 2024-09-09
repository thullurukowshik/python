a = int(input())
b = int(input())
c = int(input())
d = int(input())

if (a>b) or (c>d):
    if a>c:
        print(a)
    else:
        print(c)

else:
    if (b>a) or (d>c):
        if b>d:
            print(b)

        else:
            print(d)
