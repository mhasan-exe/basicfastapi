num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))
if num1 >= num2 and num1 >= num3:
    largest = num1
if num2 >= num1 and num2 >= num3:
    largest = num2
if num3 >= num1 and num3 >= num2:
    largest = num3
print(f"The largest number is {largest}.")