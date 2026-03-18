# =========================
# Section 1: Loop Basics
# =========================

# 1
for i in range(1, 51):
    print(i)

# 2
for i in range(1, 101):
    if i % 2 == 0:
        print(i)

# 3
for i in range(1, 101):
    if i % 2 != 0:
        print(i)

# 4
for i in range(1, 11):
    print("7 x", i, "=", 7 * i)

# 5
total = 0
for i in range(1, 101):
    total += i
print("Sum:", total)

# 6
for i in range(50, 0, -1):
    print(i)

# 7
count = 0
for i in range(1, 101):
    if i % 3 == 0:
        count += 1
print("Divisible by 3:", count)

# 8
for i in range(1, 11):
    print(i ** 2)

# 9
for i in range(1, 11):
    print(i ** 3)

# 10
n = int(input("Enter n: "))
for i in range(1, n + 1):
    print(i)


# =========================
# Section 2: While Loop
# =========================

# 11
i = 1
while i <= 20:
    print(i)
    i += 1

# 12
num = int(input("Enter number: "))
fact = 1
i = 1
while i <= num:
    fact *= i
    i += 1
print("Factorial:", fact)

# 13
num = int(input("Enter number: "))
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10
print("Reversed:", rev)

# 14
num = int(input("Enter number: "))
count = 0
while num > 0:
    count += 1
    num //= 10
print("Digits:", count)

# 15
while True:
    user = input("Enter something: ")
    if user == "stop":
        break


# =========================
# Section 3: Nested Loop
# =========================

# 16
for i in range(1, 5):
    print("*" * i)

# 17
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# 18
for i in range(1, 6):
    for j in range(1, 11):
        print(i * j, end=" ")
    print()

# 19
for i in range(3):
    print("A B C")

# 20
num = 1
for i in range(3):
    for j in range(3):
        print(num, end=" ")
        num += 1
    print()


# =========================
# Section 4: String Basics
# =========================

# 21
s = input("Enter string: ")
print("Length:", len(s))

# 22
vowels = "aeiouAEIOU"
count = 0
for ch in s:
    if ch in vowels:
        count += 1
print("Vowels:", count)

# 23
count = 0
for ch in s:
    if ch.isalpha() and ch not in vowels:
        count += 1
print("Consonants:", count)

# 24
rev = ""
for ch in s:
    rev = ch + rev
print("Reversed:", rev)

# 25
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


# =========================
# Section 5: String Slicing
# =========================

# 26
print(s[:5])

# 27
print(s[-3:])

# 28
print(s[::-1])

# 29
print(s[::2])

# 30
print(s[1:-1])


# =========================
# Section 6: List Basics
# =========================

# 31
lst = [10, 20, 30, 40, 50]
print("Sum:", sum(lst))

# 32
print("Max:", max(lst))

# 33
print("Min:", min(lst))

# 34
print("Count:", len(lst))

# 35
num = int(input("Enter number to check: "))
if num in lst:
    print("Exists")
else:
    print("Not exists")


# =========================
# Section 7: List Operations
# =========================

# 36
lst = []
lst.append(10)
lst.append(20)
lst.append(30)
print(lst)

# 37
lst.insert(1, 15)
print(lst)

# 38
lst.remove(20)
print(lst)

# 39
rev = []
for i in lst:
    rev = [i] + rev
print("Reversed:", rev)

# 40
# Bubble Sort
lst = [5, 2, 9, 1, 3]
for i in range(len(lst)):
    for j in range(len(lst) - 1):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
print("Sorted:", lst)