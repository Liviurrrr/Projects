# Student Management System
#### Video Demo:  https://youtu.be/BfUSbsvmaFM
#### Description:
This is my CS50P Final Project

This repository contains a simple Student Management System implemented in Python.
The system allows students to sign up, log in, access their information, and view a student handbook.
It uses the cryptography library for encryption, getpass for secure password input, and tabulate for tabular display.

## Features
The Student Management System provides the following features:
Sign Up: Students can create an account by providing their first name, last name, and password. Upon successful signup, the student's email is generated automatically.
Login: Registered students can log in using their email and password. Passwords are securely stored using encryption.
Student Information: Students can view their own information, including their name and email.
Student Handbook: Students can access a student handbook file (student_handbook.txt) that contains important information.
Dashboard: After logging in, students are presented with a dashboard where they can access their information and the student handbook.
Exit Codes: The system allows smooth navigation with exit codes, offering options to return to the menu or exit the program.

## Usage
The system will present a startup menu with options to log in, sign up, or exit.

If you choose to sign up, provide your first name, last name, and password.

If you choose to log in, enter your email and password.

Upon successful login, you will be directed to the dashboard, where you can access your information and the student handbook.

To exit the program at any time, follow the provided exit options.

## Benefits
User-Friendly: The system provides a simple and intuitive command-line interface for students to interact with.

Secure Password Handling: Passwords are securely handled using the getpass library, ensuring that they are not displayed in plain text.

Data Privacy: Student data is encrypted using the cryptography library, enhancing data privacy and security.

Centralized Information: The system allows students to access their information and the student handbook from a centralized dashboard.

## Limitations
Limited Authentication: The system uses basic email and password authentication, which might not be suitable for production systems requiring more advanced authentication mechanisms.

No User Management: The system lacks features like password reset, account recovery, or administrative functionalities.

Single-User: The system is designed for a single user and does not support multiple users.

Command-Line Interface: The command-line interface might not be as user-friendly as a graphical user interface (GUI) for some users.

Basic Handbook Display: The student handbook is displayed in plain text, without advanced formatting or interactive features.

Please note that this system is intended as a basic example and might not fulfill all requirements for a comprehensive student management system. It serves as a starting point for further development and customization.
