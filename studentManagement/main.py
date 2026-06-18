import student_manager as stu_m

m1 = stu_m.StudentManager()

while(1):
    print(
        "1- add student \n",
        "2- add grades\n ",
        "3- veiw all student \n",
        "4- search student\n",
        "5- update student\n ",
        "6- delete student \n",
        "7- show statistics \n",
        "8- save data \n",
        "9- exit \n")
    
    op = int(input())

    match op:
        case 1:
            st_id = input("Enter id : ")
            name = input ("Enter name: ")
            age = int(input ("Enter age: "))
            dept = input ("Enter department: ")
            
            val = m1.add_student(st_id,name,age,dept)
            print(val)

        case 2:
            st_id = input("Enter id : ")
            sub = input("Enter subject : ")
            mark = input ("Enter mark : ")
           
            val = m1.add_grades(st_id,sub,mark)
            print(val)

        case 3:
            stu = m1.view_all_student()
            print(stu)

        case 4:
            students = m1.search_student()
            print(students)

        case 5:
            stId = int(input("Enter student id: "))
            val = m1.update_student(stId)
            print(val)

        case 6:
            stId = int(input("Enter student id: "))
            val = m1.delete_student(stId)
            print(val)
        
        case 7:
            val =m1.show_statistics()
            print(val)

        case 8:
            val = m1.save_data()
            print(val)
            
        case 9:
            m1.exit()
            break
        case _:
            "Enter valid option \n"

            
