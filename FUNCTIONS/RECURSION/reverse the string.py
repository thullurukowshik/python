def is_palindrome(string,index=0):
    # Complete this recursive function
    if len(string) == index:
        return ''
    return string[-(index+1)] + is_palindrome(string,index+1)

string = input().lower()
is_true =is_palindrome(string)
print(is_true == string)
