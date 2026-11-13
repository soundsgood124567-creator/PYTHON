username = "ziyu"
password = 1234


tempname = input("Enter the username")
if tempname == username:
    tempass = int(input("Enter password : "))
    if tempass == password:
        print("login successfully")
        while True:
            print("1. Add product")
            print("2. show product")
            print("3. search product")
            choice = int(input("Enter your choice : "))
            if choice == 1:
                id = int (input("Enter product id : "))
                name = input("Enter product name : ")
                price = int (input("Enter product price : "))

            elif choice == 2:
                print (f"product id : {id}")
                print (f"product name : {name}")
                print (f"product price : {price}")

            elif choice == 3:
                print("1. Search by name  ")
                print("2.  Search by id")
                id_name = int(input("Please chose one option : "))
                if id_name == 1:
                    search_id = int(input("Enter id to search"))
                    if search_id == id:
                        print (f"product id : {id}")
                        print (f"product name : {name}")
                        print (f"product price : {price}")
                    else:
                        print("wrong id")
                elif id_name == name:
                    search_name = int(input("Enter id to search"))
                    if search_name == 2:
                        print (f"product id : {id}")
                        print (f"product name : {name}")
                        print (f"product price : {price}")
                    else:
                        print("wrong name")
            else:
                print("Invalid choice ")
                
        else:
            print("wrong username or password")
    else:
            print("wrong username or password")