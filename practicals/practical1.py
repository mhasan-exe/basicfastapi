strinput = input("Enter a string: ")
intinput = int(input("Enter an integer: "))
boolinput = input("Enter a boolean (True/False): ").strip().lower() == 'true'
floatinput = float(input("Enter a float: "))
print(f"Your value for the string is: {strinput} and its type is {type(strinput)}")
print(f"Your value for the integer is: {intinput} and its type is {type(intinput)}")
print(f"Your value for the boolean is: {boolinput} and its type is {type(boolinput)}")
print(f"Your value for the float is: {floatinput} and its type is {type(floatinput)}")