def shuffle_string(string, indexes_list):
    # complete this function
    store = ""
    indexes_list = indexes_list.split(" ")
    for index in indexes_list:
        index = int(index)
        word = string[index]
        store = store + word
    return store
            

string = input()
indexes_list = input()

result = shuffle_string(string,indexes_list)
print(result)
