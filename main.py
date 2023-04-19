import json
import os

FILE_NAME = "credentials.json"

def load_credentials(file_name):
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            return json.load(file)
    return {}

def save_credentials(credentials, file_name):
    with open(file_name, "w") as file:
        json.dump(credentials, file)

def store_credentials(credentials, category, username, password):
    if category not in credentials:
        credentials[category] = {}
    credentials[category][username] = password
    return credentials

def find_credentials(credentials, category, username):
    if category in credentials:
        return credentials[category].get(username)
    return None

def menu():
    print("1. Store new credentials")
    print("2. Retrieve password")
    print("3. Search for username")
    print("4. Quit")

def main():
    credentials = load_credentials(FILE_NAME)
    while True:
        menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            category = input("Enter the category: ")
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            credentials = store_credentials(credentials, category, username, password)
            save_credentials(credentials, FILE_NAME)
            print("Credentials stored successfully!")
        elif choice == 2:
            category = input("Enter the category: ")
            username = input("Enter the username: ")
            password = find_credentials(credentials, category, username)
            if password:
                print(f"Credentials for {username} in category {category}:")
                print(f"Username: {username}")
                print(f"Password: {password}")
            else:
                print("Username not found.")
        elif choice == 3:
            category = input("Enter the category: ")
            username = input("Enter the username: ")
            if category in credentials and username in credentials[category]:
                print(f"Username {username} found in category {category}.")
            else:
                print("Username not found.")
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
