name = input("Enter your name: ")
product = input("Enter product name: ")

sentence = f"{name} purchased {product}"
print(sentence)

print("\nLeft aligned  : ", sentence.ljust(30, "-"))
print("Right aligned : ", sentence.rjust(30, "-"))
print("Center aligned: ", sentence.center(30, "-"))