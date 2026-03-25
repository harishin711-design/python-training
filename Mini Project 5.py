visitors = set()

n = int(input("How many visitors to add? "))

for i in range(n):
    name = input("Enter visitor name: ")
    visitors.add(name)

print("Unique visitors:", visitors)
print("Total unique visitors:", len(visitors))