grades = {'Student': 'A'}

choice = input("1. Add a grade: \n2. Update a grade: \n3. Print grades: \n4. Exit\nEnter your choice: ")
while choice != '4':
    if choice == '1':
        name = input("Enter the name of the student to add: ")
        grade = input("Enter the grade for {}: ".format(name))
        grades[name] = grade
    elif choice == '2':
        name = input("Enter the name to update grade ")
        if name in grades:
            score = input("Enter the new grade for student {}: ".format(name))
            grades[name] = grade
            print("Grade {} updated for name {}.".format(grade, name))
        else:
            print("name {} not found.".format(name))
    elif choice == '3':
        print("\nCurrent grades:")
        for name, grade in grades.items():
            print("- {}: {}".format(name, grade))
        print("\n")
    else:
        print("Invalid choice. Please try again.")
    
    choice = input("1. Add a grade: \n2. Update a grade: \n3. Print grades: \n4. Exit\n")