original_variable = input("Input your string: ")
if len(original_variable) < 2:
    print("Empty String")
else:
    print(original_variable[:2]+original_variable[-2:])
