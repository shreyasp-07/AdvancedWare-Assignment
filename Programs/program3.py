import csv

def search_user_by_id_or_username(identifier):
    with open('users.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            user_id, first_name, last_name, username, email, avatar, gender, date_of_birth, *extra_values = row
            if user_id == identifier or first_name == identifier or last_name == identifier:
                return {
                    'id': user_id,
                    'first_name': first_name,
                    'last_name': last_name,
                    'username': username,
                    'email': email,
                    'avatar': avatar,
                    'gender': gender,
                    'date_of_birth': date_of_birth
                }
        return None

# Usage: Input the ID or username of a user to get their details
identifier = input("Enter the ID or username of a user: ")
user_details = search_user_by_id_or_username(identifier)
if user_details:
    print("User Details:")
    print(f"ID: {user_details['id']}")
    print(f"First Name: {user_details['first_name']}")
    print(f"Last Name: {user_details['last_name']}")
    print(f"Username: {user_details['username']}")
    print(f"Email: {user_details['email']}")
    print(f"Avatar: {user_details['avatar']}")
    print(f"Gender: {user_details['gender']}")
    print(f"Date of Birth: {user_details['date_of_birth']}")
else:
    print("User not found.")