import json

class StudentManager:

    def __init__(self):
        self.students = {}
        try:
            with open("all_students.json","r") as myfile :   # open file 
                all_students = myfile.read()   # read opened file 
                if(all_students.strip() != ""):
                    self.students = json.loads(all_students)

        except FileNotFoundError:
            self.students = {}
    

    def add_student(self,stu_id:int,name:str,age:int,dept:str) -> str:
        stu_id = str(stu_id)
        dept = dept.upper() 
        name = name.strip()
        allow_depts = ["CS","AI","SC","IS"]

        if(stu_id in self.students ):
            return "Student exist, can't put two students with same id"
        if name == "":
            return "name mustn't be empty "
        if age <= 0 :
            return "unvalid age "
        if dept not in allow_depts:
            return "unvalid department"

        self.students[stu_id] = {
            "name":name,
            "age":age,
            "department":dept,
            "grades":{}
        }

        return "Student added successfully"
    
    def add_grades(self,stu_id:int,sub:str,mark:int)->str:
        stu_id = str(stu_id)
        if(stu_id not in self.students):
            return "No student with such id"
        
        sub = sub.lower()

        if(sub in self.students[stu_id]["grades"]):
            return "subject already has a grade"
        
        self.students[stu_id]["grades"][sub] = mark

        return "grades added successfully"
    

    def menu_of_view(self)->int:
        print("1- sort by id\n",
              "2- sort by name\n",
              "3- sort by age\n"
            )
        opt = int(input())
        return opt

    def view_all_student(self)->dict:
        option = self.menu_of_view()
        if(len(self.students) == 0):
            return "No students added yet"
        
        sorted_students = self.students.copy()
        match option:
            case 1:
                sorted_students = sorted(sorted_students.items(),key = lambda x:int(x[0]))
            case 2:
                sorted_students = sorted(sorted_students.items(),key = lambda x:x[1]["name"])
            case 3:
                sorted_students = sorted(sorted_students.items(),key = lambda x:x[1]["age"])
            case _:
                return "Enter valid option !"
        
        sorted_students = dict(sorted_students) 
        return sorted_students
    
    def menu_of_search(self)->int:
        print("1- search by id\n",
              "2- search by name\n",
              "3- search by age\n"
            )
        opt = int(input())
        return opt
    
    def search_student(self)->dict:
        option = self.menu_of_search()
        search_student = {}
        match option:
            case 1:
                stu_id = input("Enter id to search for: ")
                if(stu_id in self.students):
                    search_student[stu_id] = self.students[stu_id]
                else:
                    return "no such student found"
                
            case 2:
                name = str.lower(input("Enter name to search for: "))
                for id_stu, stu_obj in self.students.items():
                    if(name in str.lower(stu_obj["name"])):
                        search_student[id_stu] = self.students[id_stu]

            case 3:
                age = int(input("Enter age to search for: "))
                for id_stu, stu_obj in self.students.items():
                    if( stu_obj["age"] == age ):
                        search_student[id_stu] = self.students[id_stu]

            case _:
                return "Enter valid option !"
        
        return search_student
    
    def update_menu(self)->int:
        print("1- update name\n",
              "2- update age\n",
              "3- update department")
        op = int(input())
        return op
    
    def update_student(self,stu_id):
        stu_id = str(stu_id)
        if(stu_id not in self.students):
            return "Student not exist\n"
        
        option = self.update_menu()
        match option:
            case 1:
                data = input("Enter student name:")
                self.students[stu_id]["name"]= data
            case 2:
                data = input("Enter student age:")
                self.students[stu_id]["age"]= data
            case 3:
                data = input("Enter student department:")
                self.students[stu_id]["dept"]= data 
            case _:
                return "Enter valid option\n"
            
        return "student updated successfully\n"

    def delete_student(self,stu_id):
        stu_id = str(stu_id)
        if(stu_id not in self.students):
            return "Student not exist\n"
        
        del self.students[stu_id]
        return "student deleted successfully"
    
    def menu_statistics()->int:
        print("1- number of students \n",
              "2- students with max Average grade\n",
              "3- number of students in each department\n")
        op = int(input())
        return op
    
    def show_statistics(self):
        option = self.menu_statistics

        n_students = len(self.students)
        n_dept ={
            "CS":0,
            "AI":0,
            "SC":0,
            "IS":0
        }
        avg = 0
        mx_avg = 0
        stu_mx = {}
        for stu_id,stu_obj in self.students.items():
            n_dept[stu_obj["department"]] += 1
            for g in stu_obj["grades"]:
                avg += g
            
            if(avg >= mx_avg ):
                stu_mx[stu_id] = stu_obj
        
        match option:
            case 1:
                return n_students
            case 2:
                return stu_mx
            case 3:
                n_dept
            case _:
                return "Enter valid option\n"
            

    def save_data(self):
        with open("all_students.json","w") as myfile :
            save_students = json.dumps(self.students)
            myfile.write(save_students)
        
        return "data saved successfully "
    
    def exit(self):
        self.save_data()








