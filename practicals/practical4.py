sub1 = int(input("Enter the  marks out of 100: "))
sub2 = int(input("Enter the  marks out of 100: "))
sub3 = int(input("Enter the marks out of 100: "))
sub4 = int(input("Enter the  marks out of 100: "))
sub5 = int(input("Enter the  marks out of 100: "))
sum = sub1 + sub2 + sub3 + sub4 + sub5
percentage = (sum / 500) * 100
if percentage >= 90:
    print("Grade: A")
elif percentage >= 80:
    print("Grade: B")
elif percentage >= 70:
    print("Grade: C")
elif percentage >= 60:
    print("Grade: D")
else:
    print("Grade: F")
print(f"The total marks obtained is: {sum}")
print(f"The percentage is: {percentage}%")