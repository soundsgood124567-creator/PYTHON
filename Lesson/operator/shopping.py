item_1 = int(input("Enter the price of the first item : "))
qua_1 = int(input("Enter the quanitity of the first item : "))
item_2 = int(input("Enter the price of the second item : "))
qua_2 = int(input("Enter the quanitity of the second item : "))
item_3 = int(input("Enter the price of the thrid item : "))
qua_3 = int(input("Enter the quanitity of the thrid item : "))
print("=====shopping bill=====")
total_1=item_1*qua_1
total2=item_2*qua_2
total_3=item_3*qua_3
print(f"first item : ${item_1*qua_1}")
print(f"second item : ${item_2*qua_2}")
print(f"thrid item : ${item_3*qua_3}")
#print(f"total price : ${(item_1*qua_1)+(item_2*qua_2)+(item_3*qua_3)}")
print(f"total price : ${total2+total_1+total_3}")