import bcrypt
import json

# File path to store user data
USER_DATA_FILE = 'user_data.json'

# Function to load user data from the file
def load_user_data():
    try:
        with open(USER_DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Function to save user data to the file
def save_user_data(users):
    with open(USER_DATA_FILE, 'w') as file:
        json.dump(users, file)

# Function to register a new user
def register_user(username, password):
    users = load_user_data()
    if username in users:
        print("Username already exists. Please choose a different one.")
    else:
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        users[username] = hashed_password.decode('utf-8')
        save_user_data(users)
        print("Registration successful. You can now log in.")

# Function to log in a user
def login_user(username, password):
    users = load_user_data()
    if username not in users:
        print("User not found. Please register first.")
        return False

    hashed_password = users[username].encode('utf-8')
    if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
        print("Login successful.")
        return True
    else:
        print("Incorrect password. Please try again.")
        return False

def main():
    while True:
        print("\nWelcome to the Task Manager!")
        print("1. Register")
        print("2. Log in")
        print("3. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            register_user(username, password)
        elif choice == '2':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if login_user(username, password):
                # Implement task management features here for logged-in users
                pass
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
