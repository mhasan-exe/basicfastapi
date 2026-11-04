value = input("Enter any value:")
if value.isdigit():
    print(f"{value} is an integer.")
elif value.isalpha():
    print(f"{value} is An Alphabet")
else:
    print(f"{value} is neither!.")