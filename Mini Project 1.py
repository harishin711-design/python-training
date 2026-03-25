employees = []


def add_employee():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    role = input("Enter role: ")
    salary = float(input("Enter salary: "))

    employee = {
        "name": name,
        "age": age,
        "role": role,
        "salary": salary
    }
    employees.append(employee)
    print("Employee added successfully.")


def display_employees():
    if not employees:
        print("No employees found.")
        return

    print("\nEmployee List")
    for i, emp in enumerate(employees, start=1):
        print(f"{i}. Name: {emp['name']}, Age: {emp['age']}, Role: {emp['role']}, Salary: {emp['salary']}")


def update_employee():
    name = input("Enter employee name to update: ")
    for emp in employees:
        if emp["name"].lower() == name.lower():
            emp["age"] = int(input("Enter new age: "))
            emp["role"] = input("Enter new role: ")
            emp["salary"] = float(input("Enter new salary: "))
            print("Employee updated successfully.")
            return
    print("Employee not found.")


def delete_employee():
    name = input("Enter employee name to delete: ")
    for emp in employees:
        if emp["name"].lower() == name.lower():
            employees.remove(emp)
            print("Employee deleted successfully.")
            return
    print("Employee not found.")


while True:
    print("\n1.Add Employee 2.Update Employee 3.Delete Employee 4.Display Employees 5.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        update_employee()
    elif choice == "3":
        delete_employee()
    elif choice == "4":
        display_employees()
    elif choice == "5":
        break
    else:
        print("Invalid choice")