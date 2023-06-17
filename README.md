# User Data Programs

This repository contains three Python programs for managing user data.

## Prerequisites

Before running the programs, make sure you have the following installed on your system:
- Python 3.x
- Requests library (`pip install requests`)

## Program 1: Get Random User Data and Write to CSV

### Description
This program makes GET requests to a random user data API and writes the retrieved data to a CSV file named `users.csv`. The data includes user information such as ID, name, email, avatar, gender, date of birth, and address.

### Steps to Run
1. Make sure you have the necessary prerequisites installed.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the program files.
4. Run the following command: `python program1.py`
5. The program will execute and fetch 10 random user data entries at an interval of 1 second.
6. The retrieved data will be stored in the `users.csv` file.

## Program 2: Calculate Age from Date of Birth in CSV

### Description
This program reads the `users.csv` file generated by Program 1 and calculates the age of each user based on their date of birth. The age is then printed for each user.

### Steps to Run
1. Make sure you have the necessary prerequisites installed.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the program files.
4. Run the following command: `python program2.py`
5. The program will read the `users.csv` file and calculate the age for each user.
6. The calculated ages will be printed on the console.

## Program 3: Search User by ID or Username

### Description
This program allows you to search for a user in the `users.csv` file based on their ID or username. If a matching user is found, their details including ID, name, username, email, avatar, gender, and date of birth will be displayed.

### Steps to Run
1. Make sure you have the necessary prerequisites installed.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the program files.
4. Run the following command: `python program3.py`
5. The program will prompt you to enter the ID or username of a user.
6. Enter the ID or username and press Enter.
7. If a user matching the input is found in the `users.csv` file, their details will be displayed.
8. If no user is found, a "User not found" message will be displayed.

