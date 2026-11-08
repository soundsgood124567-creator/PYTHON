member = input("Are you  a member ? (yes/no) : ")
total = int(input("Enter your total bill : "))
payment = input("What is your paymment method? (visa,ABA,cash)")

print ("=======recipe=======")
print (f"member  :  {member}")
print (f"Payment  :  {payment}")
print (f"total bill  :  {total}")
if member == "yes" and total >=100 :
    print("discount   : ")

