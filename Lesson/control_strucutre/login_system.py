age = int(input("enter your age : "))
grade = int(input("enter your grade : "))
if age>=18:
    if grade >=80:
        print("you passed.")
    else:
        print("your grade is not high enough.")
else:
    print("your are not old enough.")
