import requests
import time
import csv

def get_random_user_data():
    response = requests.get('https://random-data-api.com/api/users/random_user')
    if response.status_code == 200:
        return response.json()
    else:
        return None

def write_user_data_to_csv(user_data):
    address = user_data['address']
    formatted_address = f"{address['city']}, {address['state']}, {address['zip_code']}, {address['country']}"
    with open('users.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            user_data['id'],
            user_data['first_name'],
            user_data['last_name'],
            user_data['username'],
            user_data['email'],
            user_data['avatar'],
            user_data['gender'],
            user_data['date_of_birth'],
            formatted_address
        ])

def get_random_user_data_periodically(num_requests):
    for _ in range(num_requests):
        user_data = get_random_user_data()
        if user_data:
            write_user_data_to_csv(user_data)
        time.sleep(1)  # Wait for 1 second

# Get 10 random user data and write to users.csv
get_random_user_data_periodically(10)