

num = int(input("Enter a number: "))

print("Binary :", bin(num))
print("Octal  :", oct(num))
print("Hex    :", hex(num))

large_num = int(input("Enter a large number: "))
print("With commas:", f"{large_num:,}")

scientific_num = float(input("Enter number for scientific notation: "))
print("Scientific notation:", f"{scientific_num:e}")