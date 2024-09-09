def get_reversed_string(string,index=0,result=""):
    # Complete this recursive function
    if len(string) == (index):
        return result
    return result + string[-(index+1)] + get_reversed_string(string,index+1)

string = input()

resultant_string =get_reversed_string(string)
print(resultant_string)
