def get_lower_and_upper_case_letters(word):
    upp_store = ""
    low_store =""
    
    for i in word:
        if i.isupper():
            upp_store = upp_store + i
        else:
            low_store = low_store + i
    print(upp_store)
    print(low_store)

word = input()
get_lower_and_upper_case_letters(word)
