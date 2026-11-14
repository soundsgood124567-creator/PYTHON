stu_id = None
stu_name = ""
stu_grade = ""
stu_gender = ""
stu_level = None
while True:
    print("1. student")
    print("2. teacher")
    print("3. exit")
    stu_teacher = int(input("Enter your choice(1,2,3) : "))

    match stu_teacher:
        case 1:
            print("1. Add student")
            print("2. Show student")
            print("3. search student")
            print("4. update student")
            print("5. delete student")
            print("6. exit")

            stu_choice = int(input("Enter a choice : "))
            match stu_choice:
                case 1:
                    stu_id = int(input("Enter student id : "))
                    stu_name = input("Enter student name : ")
                    stu_grade = input("Enter student grade : ")
                    stu_gender = input("Enter student gender : ")
                    stu_level = int(input("Enter student level : "))
                case 2: 
                    print(f"student id : {stu_id}")
                    print(f"student name : {stu_name}")
                    print(f"student grade : {stu_grade}")
                    print(f"student gender : {stu_gender}")
                    print(f"student level : {stu_level}")
                case 3:
                    search_id = int(input("Enter stuent id the search : "))
                    if search_id == stu_id:
                        print(f"student id : {stu_id}")
                        print(f"student name : {stu_name}")
                        print(f"student grade : {stu_grade}")
                        print(f"student gender : {stu_gender}")
                        print(f"student level : {stu_level}")
                    else :
                        print("student not found")
                case 4 :
                    update_id=int(input("Enter student id to update : "))
                    if update_id == stu_id:
                        stu_id = int(input("Enter student id : "))
                        stu_name = input("Enter student name : ")
                        stu_grade = input("Enter student grade : ")
                        stu_gender = input("Enter student gender : ")
                        stu_level = int(input("Enter student level : "))
                    else :
                        print("student not found")
                case 5 : 
                    del_id = int(input("Enter student id to delete "))
                    if del_id == stu_id:
                        stu_id = " "
                        stu_name = " "
                        stu_gender = " "
                        stu_level=" "
                        stu_grade = " "
                case 6:
                    break

        case 2:
                print("1. Add teacher")
                print("2. Show teacher")
                print("3. search teacher")
                print("4. update teacher")
                print("5. delete teacher")
                print("6. exit")

                stu_choice = int(input("Enter a choice : "))
                match stu_choice:
                    case 1:
                        tea_id = int(input("Enter teacher id : "))
                        tea_name = input("Enter teacher name : ")
                        tea_age = int(input("Enter teacher age : "))
                        tea_subject = input("Enter teacher subject : ")
                        tea_exp = int(input("Enter teacher experenice(year) : "))
                        tea_phone = int(input("Enter teacher phone number : "))
                    case 2: 
                        print(f"teacher id : {tea_id}")
                        print(f"teacher name : {tea_name}")
                        print(f"teacher age : {tea_age}")
                        print(f"teacher subject : {tea_subject}")
                        print(f"teacher experenice : {tea_exp}")
                        print(f"teacher phone number : {tea_phone}")
                    case 3:
                        search_id = int(input("Enter teacher id the search : "))
                        if search_id == tea_id:
                            print(f"teacher id : {tea_id}")
                            print(f"teacher name : {tea_name}")
                            print(f"teacher age : {tea_age}")
                            print(f"teacher subject : {tea_subject}")
                            print(f"teacher experenice : {tea_exp}")
                            print(f"teacher phone number : {tea_phone}")
                        else :
                            print("teacher not found")
                    case 4 :
                        update_id=int(input("Enter teacher id to update : "))
                        if update_id == tea_id:
                            tea_id = int(input("Enter teacher id : "))
                            tea_name = input("Enter teacher name : ")
                            tea_age = int(input("Enter teacher age : "))
                            tea_subject = input("Enter teacher subject : ")
                            tea_exp = int(input("Enter teacher experenice(year) : "))
                            tea_phone = int(input("Enter teacher phone number : "))
                        else :
                            print("teacher not found")
                    case 5 : 
                        del_id = int(input("Enter teacher id to delete "))
                        if del_id == tea_id:
                            tea_id = " "
                            tea_name = " "
                            tea_age = " "
                            tea_subject=" "
                            tea_exp = " "
                            tea_phone = " "
                        else :
                           print("teacher not found")
                    case 6:
                        break



            