Student = {}

while True:
    print("\n------STUDENT MANAGER APP------")
    print("1.add student")
    print("2.view student")
    print("3.chek result")
    print("4.Exit")

    choice = input("Enter your choice: ")

    #Add student
    if choice =="1":
        name = input("Enter student name: ")
        marks = int(input("Enter marks"))
        Student [name] = marks
        print(f"{name} successfully added!")

     #view student
    elif choice =="2":
        if not Student:
            print("no student found!")
        else:
            for name,marks in Student.items():
                print(name,":",marks)  

    #check result
    elif choice =="3":
        name=input("Enter student name")

        if name in Student:
            marks = Student[name]

            if marks >=40:
                print("PASS")
            else:
                print("FAIL")

        else:
            print("student Not found!")            


    #exit
    elif choice =="4":
        print("Exitiin......")
        break
    else:
        print("In-valid input")            