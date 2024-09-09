def validate_atm_pin_code(pin):
    count=0
    no_of_digits=0
    for i in pin:
        if i.isdigit():
            count= count+1
        else:
            no_of_digits=no_of_digits +1
            break
    if (count==4 or count==6):
        if (no_of_digits==0):
            print("Valid PIN Code")
    else:
        print("Invalid PIN Code")

pin =input()
validate_atm_pin_code(pin)
