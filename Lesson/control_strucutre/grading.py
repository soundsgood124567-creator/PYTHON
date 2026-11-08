name = input("Enter your name : ")
age = input("Enter your age : ")
gender = input("Enter your gender : ")
level = input("Enter your level : ")
math = int(input("Enter your math score : "))
English = int(input("Enter your English score : "))
khmer = int(input("Enter your khmer score : "))
chinese = int(input("Enter your Chinese score : "))
total = math + khmer + chinese + English
average =total/4
print(f"Average score : {average}")

if average <= 100 and average >=90 :
    print("Grade A")
elif average <= 89 and average >= 80:
    print ("Grade B")
elif average <=79 and average >=70:
    print("Grade c")
elif average <=69 and average >=60:
    print ("Grade D")
else :
    print ("Grade F")

   
   
