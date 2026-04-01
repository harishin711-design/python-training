# =========================================
# Task 1: Encapsulation (User Class)
# =========================================

class User:
    def __init__(self):
        self.__user_name = ""
        self.__pwd = ""

    def set_user(self, user_name, pwd):
        self.__user_name = user_name
        self.__pwd = pwd

    def get_user(self):
        return self.__user_name

    def register(self):
        print(f"Registering user: {self.__user_name}")

    def login(self):
        print(f"Logging in: {self.__user_name}")


print("Task 1:")
user1 = User()
user1.set_user("john", "1234")
user1.register()
user1.login()
print("Username:", user1.get_user())


# =========================================
# Task 2: Inheritance (User → Student, Faculty)
# =========================================

class User:
    def register(self):
        print("User registered")

    def login(self):
        print("User logged in")


class Student(User):
    def student_greet(self):
        print("Hello Student")


class Faculty(User):
    def faculty_greet(self):
        print("Hello Faculty")


class TempFaculty(Faculty):
    def tempFaculty_greet(self):
        print("Hello Temp Faculty")


print("\nTask 2:")
student = Student()
faculty = Faculty()
temp_faculty = TempFaculty()

print("Student Object:")
student.register()
student.login()
student.student_greet()

print("\nFaculty Object:")
faculty.register()
faculty.login()
faculty.faculty_greet()

print("\nTempFaculty Object:")
temp_faculty.register()
temp_faculty.login()
temp_faculty.faculty_greet()
temp_faculty.tempFaculty_greet()

print("\nParent cannot access child methods directly")
parent = User()
parent.register()
parent.login()
# parent.student_greet()   # Not possible
# parent.faculty_greet()   # Not possible


# =========================================
# Task 3: Method Overriding
# =========================================

class User:
    def greet(self):
        print("Welcome User")


class Student(User):
    def greet(self):
        print("Welcome Student")


class Faculty(User):
    def greet(self):
        print("Welcome Faculty")


print("\nTask 3:")
student = Student()
faculty = Faculty()
user = User()

user.greet()
student.greet()
faculty.greet()


# =========================================
# Task 4: Method Chaining
# =========================================

class User:
    def register(self):
        print("registered")
        return self

    def login(self):
        print("logined")
        return self

    def greet(self):
        print("enjoy everyone")
        return self


print("\nTask 4:")
user = User()
user.login().greet().register()


# =========================================
# Task 5: Combined Task (Real-Time)
# =========================================

class User:
    users_count = 0

    def __init__(self, user_name, pwd):
        self.__user_name = user_name
        self.__pwd = pwd
        User.users_count += 1

    def get_user(self):
        return self.__user_name

    def set_user(self, user_name, pwd):
        self.__user_name = user_name
        self.__pwd = pwd

    def register(self):
        print(f"{self.__user_name} registered")
        return self

    def login(self):
        print(f"{self.__user_name} logined")
        return self

    def greet(self):
        print("Welcome User")
        return self


class Student(User):
    def greet(self):
        print("Welcome Student")
        return self


class Faculty(User):
    def greet(self):
        print("Welcome Faculty")
        return self


print("\nTask 5:")
user1 = User("harish", "1111")
student1 = Student("meena", "2222")
faculty1 = Faculty("ravi", "3333")

user1.login().greet().register()
student1.login().greet().register()
faculty1.login().greet().register()

print("Total users created:", User.users_count)
print("Student username:", student1.get_user())
print("Faculty username:", faculty1.get_user())