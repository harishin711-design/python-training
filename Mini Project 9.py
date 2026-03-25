students = {}


def add_student():
    name = input("Enter student name: ")
    courses = input("Enter courses separated by comma: ").split(",")
    students[name] = [course.strip() for course in courses]
    print("Student added successfully.")


def update_courses():
    name = input("Enter student name to update: ")
    if name in students:
        courses = input("Enter new courses separated by comma: ").split(",")
        students[name] = [course.strip() for course in courses]
        print("Courses updated successfully.")
    else:
        print("Student not found.")


def display_students():
    if not students:
        print("No student records found.")
        return

    for name, courses in students.items():
        print(f"{name}: {courses}")


while True:
    print("\n1.Add Student 2.Update Courses 3.Display Students 4.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        update_courses()
    elif choice == "3":
        display_students()
    elif choice == "4":
        break
    else:
        print("Invalid choice")