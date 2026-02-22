"""
User Login System
Poshun Lin
A simple user login system that checks for valid usernames and passwords, and assigns security levels based on the username. 
The system allows for three attempts to enter the correct password before denying access.
No starter code
02/22/2026

"""

users = {
    "guest": "guest",
    "alice": "alice123",
    "bob": "bob987",
    "steve": "steve456"
}

username = input("Enter your username: ")

if username not in users:
    print("Error: Username not found.")
    exit()


attempts = 3

while attempts > 0:
    password = input("Enter your password: ")
    
    if users[username] == password:
        if username == "guest":
            security_level = "Guest"
        else:
            security_level = "Security Level 1"
        
        print(f"Welcome, {username}!")
        print(f"Your security level is: {security_level}")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Incorrect password. {attempts} attempt(s) remaining.")
        else:
            print("Incorrect password. No attempts remaining.")
            print("Access Denied")
            exit()
