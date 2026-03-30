# =========================================
# Task 1: User Info Manager (Functions + Dictionary)
# =========================================

def create_user(name, age, role):
    user = {
        "name": name.title(),
        "age": age,
        "role": role
    }
    return user

users = []

users.append(create_user("harish", 22, "developer"))
users.append(create_user("meena", 20, "tester"))
users.append(create_user("ravi", 25, "designer"))

print("Task 1: All Users")
for user in users:
    print(user)


# =========================================
# Task 2: Dynamic Calculator (*args)
# =========================================

def calculate_total(*numbers):
    total = sum(numbers)
    average = total / len(numbers) if len(numbers) > 0 else 0
    return total, average

total, average = calculate_total(10, 20, 30, 40, 50)
print("\nTask 2:")
print("Total:", total)
print("Average:", average)


# =========================================
# Task 3: Keyword Config System (**kwargs)
# =========================================

def system_config(**settings):
    print("\nTask 3:")
    for key, value in settings.items():
        print(f"{key}: {value}")

system_config(mode="debug", version="1.0", theme="dark")


# =========================================
# Task 4: Factorial Service (Recursion)
# =========================================

def factorial(n):
    if n < 0:
        return "Error: Factorial not defined for negative numbers"
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print("\nTask 4:")
print("Factorial of 5:", factorial(5))
print("Factorial of 0:", factorial(0))
print("Factorial of -3:", factorial(-3))


# =========================================
# Task 5: Memory Optimization (Generator)
# =========================================

def square_generator(n):
    for i in range(1, n + 1):
        yield i * i

print("\nTask 5:")
normal_list = [i * i for i in range(1, 6)]
gen = square_generator(5)

print("Normal List:", normal_list)
print("List Type:", type(normal_list))
print("Generator Type:", type(gen))

print("Generator Values:")
for value in gen:
    print(value)


# =========================================
# Task 6: Exception Handling Module
# =========================================

print("\nTask 6:")
try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    result = numerator / denominator
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
except ValueError:
    print("Error: Invalid input, please enter numbers only")
finally:
    print("Program Completed")


# =========================================
# Task 7: File Handling
# =========================================

print("\nTask 7:")

with open("team_data.txt", "w") as file:
    file.write("Name: Harish, Age: 22, Role: Developer\n")
    file.write("Name: Meena, Age: 20, Role: Tester\n")
    file.write("Name: Ravi, Age: 25, Role: Designer\n")

print("File closed after writing:", file.closed)

with open("team_data.txt", "r") as file:
    content = file.read()
    print("File Content:")
    print(content)

print("File closed after reading:", file.closed)