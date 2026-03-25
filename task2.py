# =========================
# Bitwise Operator Tasks
# =========================

# 1
a = 10
b = 6
print("1.", a & b)

# 2
x = 12
y = 5
print("2.", x | y)

# 3
num = 8
print("3.", ~num)

# 4
a = 15
b = 9
print("4.", a ^ b)

# 5
num = 7
print("5.", num << 2)

# 6
num = 20
print("6.", num >> 1)

# 7
a = int(input("7. Enter first number: "))
b = int(input("7. Enter second number: "))
print("AND result =", a & b)

# 8
a = int(input("8. Enter first number: "))
b = int(input("8. Enter second number: "))
print("XOR result =", a ^ b)


# =========================
# String Tasks
# =========================

# 9
s = "hi"
print("9.", s * 4)

# 10
s = "python"
print("10.", s * 3)

# 11
a = "super"
b = "man"
print("11.", a + b)

# 12
a = "hello"
b = " "
c = "world"
print("12.", a + b + c)

# 13
name = input("13. Enter your name: ")
print("13.", name * 5)

# 14
str1 = input("14. Enter first string: ")
str2 = input("14. Enter second string: ")
print("14.", str1 + str2)


# =========================
# Input & Type Casting Tasks
# =========================

# 15
name = input("15. Enter your name: ")
print("15.", type(name))

# 16
age = int(input("16. Enter age: "))
print("16.", age)

# 17
a = int(input("17. Enter first number: "))
b = int(input("17. Enter second number: "))
print("17. Sum =", a + b)

# 18
m1 = float(input("18. Enter first mark: "))
m2 = float(input("18. Enter second mark: "))
print("18. Average =", (m1 + m2) / 2)

# 19
a = int(input("19. Enter value of a: "))
b = int(input("19. Enter value of b: "))
print("19.", 3 * a * 2 + b - 2)

# 20
num = input("20. Enter a number: ")
print("Before type casting:", type(num))
num = int(num)
print("After type casting:", type(num))


# =========================
# Unit Digit Tasks
# =========================

# 21
num = input("21. Enter a number: ")
print("21. Last digit =", num[-1])

# 22
num = int(input("22. Enter a number: "))
print("22. Unit digit =", num % 10)

# 23
num = int(input("23. Enter a number: "))
print("23. Number after removing last digit =", num // 10)

# 24
num = int(input("24. Enter a number: "))
print("24. Second last digit =", (num // 10) % 10)

# 25
num = int(input("25. Enter a 5-digit number: "))
print("25. Last digit =", num % 10)


# =========================
# If Statement Tasks
# =========================

# 26
if 10 >= 5:
    print("26. 10 is greater than or equal to 5")

# 27
num = int(input("27. Enter a number: "))
if num > 50:
    print("27. Number is greater than 50")

# 28
age = int(input("28. Enter age: "))
if age >= 18:
    print("28. Eligible")

# 29
num = int(input("29. Enter a number: "))
if num > 100:
    print("29. Number is greater than 100")

# 30
num = int(input("30. Enter a number: "))
if num >= 0:
    print("30. Number is non-negative")


# =========================
# If-Else Tasks
# =========================

# 31
num = int(input("31. Enter a number: "))
if num % 2 == 0:
    print("31. Even")
else:
    print("31. Odd")

# 32
marks = int(input("32. Enter marks: "))
if marks >= 35:
    print("32. Pass")
else:
    print("32. Fail")

# 33
num = int(input("33. Enter a number: "))
if num >= 0:
    print("33. Positive")
else:
    print("33. Negative")

# 34
num = int(input("34. Enter a number: "))
if num > 10:
    print("34. Greater than 10")
else:
    print("34. Not greater than 10")


# =========================
# Nested If Tasks
# =========================

# 35
age = int(input("35. Enter age: "))
height = int(input("35. Enter height: "))
weight = int(input("35. Enter weight: "))

if age >= 18:
    if height >= 160:
        if weight >= 60:
            print("35. Selected")
        else:
            print("35. Rejected")
    else:
        print("35. Rejected")
else:
    print("35. Rejected")

# 36
marks = int(input("36. Enter marks: "))
age = int(input("36. Enter age: "))

if marks >= 60:
    if age >= 17:
        print("36. Admission Granted")
    else:
        print("36. Admission Rejected")
else:
    print("36. Admission Rejected")

# 37
age = int(input("37. Enter age: "))
height = int(input("37. Enter height: "))
weight = int(input("37. Enter weight: "))

if age >= 16:
    if height >= 150:
        if weight >= 50:
            print("37. Selected")
        else:
            print("37. Rejected")
    else:
        print("37. Rejected")
else:
    print("37. Rejected")


# =========================
# Match Statement Tasks
# =========================

# 38
day = int(input("38. Enter number (1-7): "))
match day:
    case 1:
        print("38. Monday")
    case 2:
        print("38. Tuesday")
    case 3:
        print("38. Wednesday")
    case 4:
        print("38. Thursday")
    case 5:
        print("38. Friday")
    case 6:
        print("38. Saturday")
    case 7:
        print("38. Sunday")
    case _:
        print("38. Invalid input")

# 39
color = int(input("39. Enter number (1-3): "))
match color:
    case 1:
        print("39. Red")
    case 2:
        print("39. Blue")
    case 3:
        print("39. Green")
    case _:
        print("39. Invalid input")

# 40
fruit = int(input("40. Enter number (1-4): "))
match fruit:
    case 1:
        print("40. Apple")
    case 2:
        print("40. Mango")
    case 3:
        print("40. Orange")
    case 4:
        print("40. Banana")
    case _:
        print("40. Invalid input")