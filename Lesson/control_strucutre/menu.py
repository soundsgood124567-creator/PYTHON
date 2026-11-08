print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Divison")
print("5. Exits")
menu = int(input("Enter your choice : "))
number1 = float(input("Eneter a number : "))
number2 = float(input("Eneter a number : "))

if menu == 1 : 
    print(f"addition : {  number1 + number2}")
elif menu == 2 :

    print(f"subttracion : {number1 - number2}")
elif menu ==3 :
     print(f"Multiplication : {number1 * number2}")
elif menu ==4 :
     print(f"Divison : {number1 / number2}")
elif menu ==5 :
     exit