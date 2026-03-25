users = {
    "harish": "1234",
    "admin": "admin123",
    "user1": "pass1"
}

username = input("Enter username: ")
password = input("Enter password: ")

if username in users and users[username] == password:
    print("Login successful")
else:
    print("Invalid username or password")