word = input()
vowels=('a','e','i','o','u','A','E','I','O','U')
for i in word:
    if i in vowels:
        word=word.replace(i,"")
print(word)
