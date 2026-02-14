students = []

def add_student():
    roll = int(input("enter Roll No: "))
    name = input("Enter Name: ")
    branch = input("Enter branch: ")
    marks = input("Enter 3 subjects marks seperated by space: ").split()
    marks = list(map(int,marks))
    email = input("Enter Email: ")
    student = { 'roll': roll, 'name': name, 'branch': branch, 'marks':marks, 'email': email}
    students.append(student)
    print("student added sucessfully!:\n")

def display_all():
    if not students:
        print("No students records avaiable.\n")
        return
    for student in students:
        print("-"  * 40)  
        print(f"Roll No      : {student['roll']}")   
        print(f"Name         : {student['name']}")   
        print(f"Branch       : {student['branch']}")   
        print(f"Marks        : {student['marks']}")   
        print(f"Email        : {student['email']}")   
        print(f"Total        : {sum(student['marks'])}")   
        print(f"Average      : {sum(student['marks'])/len(student['marks']):.2f}")
    print()
def search_student():
    rno = int(input("enter Roll No to search: "))
    for student in students:
        if student['roll'] == rno:
            print(f"\nStudent Found :{student}\n") 
            return 
    print("Student not found.\n")   
def update_student():
    rno = int(input("enter Roll No is update: ")) 
    for student in students:
        if student['roll'] == rno:
            print("what do you want to update?")  
            print("1. Name\n2. Branch\n3. Marks\n4. Email")
            choice = input("enter choice: ")  
            if choice == '1':
                student['name'] = input("Enter new name: ") 
            elif choice == '2':
                student['branch'] = input("enter new branch: ")     
            elif choice == '3':
                marks = input("Enter 3 new marks: ").split() 
                student['marks'] = list(map(int,marks)) 
            elif choice == '4':
                student['email'] = input("enter new email: ") 
            else: print("Invalid choice!")  
            print("update sucessfully!\n")  
            
            return
    print("Student not found.\n")   
    
def delete_student(): 
    rno = int(input("Enter Roll No to delete: "))
    global students
    original_length = len(students)
    students = [s for s in students if s['roll'] != rno]
    if len(students) < original_length:
        print("Student deleted sucessfullt.\n")
    else: 
        print("Student not found.\n")    
def filter_by_marks():
    threshold = int(input("Enter mark threshold (Total): "))
    print(f"\nStudents scoring above {threshold};")  
    for student in students:
        total = sum(student['marks']) 
        if total >= threshold:
            print(f"{student['name']} | total:{total}") 
    print()
    
def show_topper():
    if not students:
        print("No student records.\n")
        return
    topper = max(students, key=lambda s: sum(s['marks'])) 
    print(f"\nTopper is:{topper['name']} with total {sum(topper['marks'])}\n") 
    
def menu():
    while True:
        print("===Student InfoBot ===") 
        print("1. Add Student ") 
        print("2. Display All students ")
        print("3. Search by Roll No ")
        print("4. Update Student  ")
        print("5. Delete Student ")
        print("6. Filter by Total Marks ")
        print("7. Show Topper ")
        print("8. Exit ")
        choice = input("enter Your choice: ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            display_all()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            filter_by_marks()
        elif choice == '7':
            show_topper()
        elif choice == '8':
            print("Exiting... Thank you!") 
            break 
        else:
            print("Invalid choice. Try again.\n")  
            
            
            
menu()                                    
                    
                