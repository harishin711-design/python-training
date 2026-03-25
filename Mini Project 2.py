def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "Fail"


def report_card():
    name = input("Enter student name: ")
    m1 = int(input("Enter mark 1: "))
    m2 = int(input("Enter mark 2: "))
    m3 = int(input("Enter mark 3: "))

    total = m1 + m2 + m3
    average = total / 3
    grade = calculate_grade(average)

    print("\n----- Report Card -----")
    print(f"Name    : {name}")
    print(f"Marks   : {m1}, {m2}, {m3}")
    print(f"Total   : {total}")
    print(f"Average : {average:.2f}")
    print(f"Grade   : {grade}")


report_card()