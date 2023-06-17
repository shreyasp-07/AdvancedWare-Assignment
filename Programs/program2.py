import csv
from datetime import datetime

def calculate_age(date_of_birth):
    dob = datetime.strptime(date_of_birth, '%Y-%m-%d')
    today = datetime.today()
    age = today.year - dob.year
    if today.month < dob.month or (today.month == dob.month and today.day < dob.day):
        age -= 1
    return age

def read_users_csv():
    with open('users.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            user_id, first_name, last_name, username, email, avatar, gender, date_of_birth, *extra_values = row
            age = calculate_age(date_of_birth)
            print(f"User ID: {user_id}, Age: {age}")

# Usage: Read "users.csv" and calculate age for each user
read_users_csv()