phone_number = input("Enter the phone number: ")
if phone_number.isdecimal():
    if len(phone_number) == 10:
        print("Correctly")
    else:
        print("The phone number must contain 10 digits ")
else:
    print("The phone number must contain only digits")


