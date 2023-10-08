from cryptography.fernet import Fernet
from getpass import getpass
from tabulate import tabulate
import sys
import csv
import re

DATA_FILE = "student_info.csv"
HAND_BOOK = "student_handbook.txt"


# Student class
class Student():
    def __init__(self, first_name=None, last_name=None, password=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = f"{first_name}.{last_name}@myschool.edu"
        self.password = password

    def signup_details(self, signup_key, signup_password):
        key = re.search(r"^b'(.+)'$", signup_key)
        password = re.search(r"^b'(.+)'$", signup_password)
        with open(DATA_FILE, "a") as file:
            file.write(
                f"{self.first_name},{self.last_name},{self.email},{key.group(1)},{password.group(1)}\n"
                )

    def student_info(self, email):
        with open(DATA_FILE, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                csv_email = row[2].strip().lower()
                input_email = email.strip().lower()

                if input_email == csv_email:
                    print(f"Name: {row[0].capitalize()} {row[1].capitalize()}")
                    print(f"Email: {email}")
                else:
                    continue


def main():
    email = startup()
    dashboard(email)

def exit_code():
    sys.exit("Exiting the system...")

# Startup screen or menu
def startup():
    print("Welcome to student system.")
    first_page = [[1, "login"], [2, "signup"], [3, "exit"]]
    print(tabulate(first_page, tablefmt="rounded_grid"))

    choice = input("Enter your choice: ")
    while True:
        if choice == "1":
            email = login()
            return email
        elif choice == "2":
            signup()
            break
        elif choice == "3":
            exit_code()
        else:
            choice = input("Enter a valid choice: ")
            continue


# login
def login():
    running = True

    while running:
        email = input("Email: ")
        password = getpass("Password: ")

        with open(DATA_FILE, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if email == row[2]:
                    # converting to bytes
                    key = bytes(row[3], encoding="utf-8")
                    encrypted_password = bytes(row[4], encoding="utf-8")

                    # decryption
                    crypter = Fernet(key)
                    pw = crypter.decrypt(encrypted_password)
                    passw = str(pw, "utf-8")

                    # verification
                    if password == passw:
                        running = False
                        return email
                    else:
                        print("Incorrect password")
                        break
                else:
                    continue

            if email not in row:
                print("Invalid email, Try again")


# signup
def signup():
    first_name = input("First name: ").lower().strip()
    last_name = input("Last name: ").lower().strip()

    # confirm password
    while True:
        passw = getpass("Password: ")
        confirm_passw = getpass("Confirm Password: ")

        if passw == confirm_passw:
            pw = passw
            break
        else:
            print("Passwords do not match, try again.")
            continue

    key = Fernet.generate_key()
    crypter = Fernet(key)
    password = crypter.encrypt(bytes(pw, encoding="utf-8"))

    # print email to use for login
    new_student = Student(first_name, last_name, password)
    print()
    print(f"Your student email is {new_student.email}")

    new_student.signup_details(str(key), str(password))

    # signup exit codes
    while True:
        menu = input("Press m to go to menu or x to exit program: ")
        if menu in ["m", "M"]:
            startup()
            break
        elif menu in ["x", "X"]:
            while True:
                sure = input("Are you sure you want to go (Y/N): ")
                if sure in ["y", "Y"]:
                    sys.exit()
                elif sure in ["n", "N"]:
                    break
                else:
                    pass
        else:
            pass


def dashboard(email):
    print()
    print("Welcome to dashboard!")
    first_page = [
        [1, "Student Information"],
        [2, "Student Hand Book"],
        [3, "Menu"],
    ]
    print(tabulate(first_page, tablefmt="rounded_grid"))

    choice = input("Enter your choice: ")
    if choice == "1":
        student_info(email)
    if choice == "2":
        student_hand_book(email)
    if choice == "3":
        main()


def exit_codes(email):
    # student_info exit codes
    while True:
        menu = input("Press d to go to dashboard or x to exit program: ")
        if menu in ["d", "D"]:
            dashboard(email)
            break
        elif menu in ["x", "X"]:
            while True:
                sure = input("Are you sure you want to go (Y/N): ")
                if sure in ["y", "Y"]:
                    exit_code()
                elif sure in ["n", "N"]:
                    break
                else:
                    pass
        else:
            pass


def student_info(email):
    student = Student()
    student.student_info(email)
    exit_codes(email)


def student_hand_book(email):
    print()
    print(("*" * 10) + " STUDENT HANDBOOK " + ("*" * 10))
    print()
    try:
        with open(HAND_BOOK, "r") as file:
            lines = file.readlines()
            for line in lines:
                print(line.rstrip())
    except FileNotFoundError:
        print("Sorry, File Not Found")
    exit_codes(email)


if __name__ == "__main__":
    main()
