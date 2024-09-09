def number_of_cars_needed(no_of_people):
    # Complete this function
    if no_of_people%5==0:
        cars_need = no_of_people//5
    else:
        if no_of_people%5 <5:
             m = no_of_people // 5 
             cars_need = m + 1
    print(cars_need)


no_of_people = int(input())
number_of_cars_needed(no_of_people)
