word_1 = input()
word_2 = input()
length_1 = len(word_1)
length_2 = len(word_2)
for i in range(1,length_1+1):
    first = word_1[-i:]
    second = word_2[:i]
    if first == second:
        print(first)
        break
if first!=second:
    print("No overlapping")
