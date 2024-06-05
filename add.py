import string
import random
import pwinput
from filehandler import display_file_options, select_file, store_in_file
from exithandler import program_exit

''' Function to generate a random password given the password length '''
def generate_password():
    char_set = string.digits + string.ascii_letters
    password_length = int(input(">\tEnter desired length of password (int): "))
    toggle_punct = input(">\tInclude special characters in password? (y/n): ").upper()
    
    if toggle_punct == 'Y':
        char_set += string.punctuation
        
    random_password = ''.join(random.sample(char_set*password_length, password_length))
    return random_password

''' Function to enter account information '''
def enter_account_info():
    print("Type 'none' if email or username is not applicable.")
    print("To generate a random password, type 'gen()' for both password & password confirm.\n")
    header = input(">\t1. Name the account header: ")
    if header == "" or header == "none":
        program_exit("Header cannot be empty or none")
    
    email = input(">\t2. Enter email: ")
    if email == "":
        program_exit("Email cannot be empty")
    
    username = input(">\t3. Enter username: ")
    if username == "":
        program_exit("Username cannot be empty")
    
    if email == "none" and username == "none":
        program_exit("Email and username cannot both be none")
    
    # password = pwinput.pwinput(prompt=">\t4. Enter password: ")
    password = input(">\t4. Enter password: ")
    if password == "":
        program_exit("Password cannot be empty")
    
    # password_confirm = pwinput.pwinput(prompt=">\t5. Confirm password: ")
    password_confirm = input(">\t5. Confirm password: ")
    if password_confirm != password:
        program_exit("Passwords do not match")

    if password == "gen()" and password_confirm == "gen()":
        password = generate_password()
        print(f"\nGenerated password: {password}")
    
    print(f"\nSummary:")
    print(f"\tHeader:\t\t{header}")
    print(f"\tEmail:\t\t{email}")
    print(f"\tUsername:\t{username}")
    print(f"\tPassword:\t{password}")
    return header, email, username, password

''' Function to add an account '''
def add_account():
    display_file_options()
    file_name, file_path = select_file("add account to")
    print(f"\n\n\n---------- ADDING ACCOUNT TO '{file_name}' ----------\n")
    header, email, username, password = enter_account_info()
    store_in_file(file_name, file_path, header, email, username, password)