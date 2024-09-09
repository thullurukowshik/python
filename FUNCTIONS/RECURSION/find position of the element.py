def get_index(x,y,index=0):
     # Complete this recursive function
     if int(x[index]) == y:
         return index
     return  get_index(x,y,index+1)
     
numbers_list = input().split(" ")
number = int(input())
number_index =get_index(numbers_list,number)
print(number_index)
