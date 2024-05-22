'''
Password Manager Structure

Core Features:
1. Add account entry to txt file
    - Account Entry Format: <header> : <email> <username> <password>
    - <header> = header name of the account (i.e. Gmail Account)
    - <email> = email of account
    - <username> = username of account
    - <password> = password of account
    - Sepatae each entry with an empty line
2. Edit passwords of existing account?
3. Salt passwords and hash passwords?
4. Password generator
    - Arguments: keywords
'''

import time
import os
import pwinput

''' Function to handle program exits '''
def program_exit(error):
    print(f"{error} -> Program exiting...")
    time.sleep(1)
    print("Goodbye.")
    exit(0)

''' Function to display Password Manager menu '''
def display_menu():
    print("\n----- PASSWORD MANAGER MENU -----\n")
    print("->\t1. Add an account")
    print("->\t2. View accounts")
    print("->\t3. Exit program")
    print("\n---------------------------------\n")

''' Function to select menu option '''
def menu_select():
    selected_option = int(input("Select a menu option: "))
    print(f"You entered option {selected_option}.")
    return selected_option

''' Function to enter account information '''
def enter_account_info():
    print("\n----- ADD AN ACCOUNT -----\n")
    header = input("Name account header: ")
    email = input("Enter email: ")
    username = input("Enter username: ")
    # password = pwinput.pwinput(prompt="Enter password: ")
    # password_confirm = pwinput.pwinput(prompt="Confirm password: ")
    password = input("Enter password: ")
    password_confirm = input("Confirm password: ")

    if password_confirm != password:
        program_exit("\nPasswords do not match")
    
    else:
        print("\nSuccess!")
        return header, email, username, password

''' Function to display the file options '''
def display_file_options():
    print("\n----- ACCOUNT FILE OPTIONS -----\n")
    print("->\taccounts_csuf.txt")
    print("->\taccounts_job.txt")
    print("->\taccounts_software.txt")
    print("\n--------------------------------\n")

''' Function to select the file to add account entry to '''
def select_file():
    try:
        file_name = input("Enter name of a file to add account to (i.e. csuf, job, software): ")
        valid_file_names = ["csuf", "job", "software"]
        
        if file_name not in valid_file_names:
            print("\nInvalid file name. Try again.")
        
        else:
            file_name = "accounts_" + file_name + ".txt"
            file_path = os.path.join("Documents", file_name)
            print(f"File path: {file_path}")
            return file_path
    
    except KeyboardInterrupt:
        program_exit("\n\nKeyboardInterrupt")

''' Function to read file to see if a header already exists '''
def read_file(file_path):
    pass

''' Function to store account entry in the file '''
def store_in_file(file_path):
    file_path = select_file()
    file_append = open(file_path, "a")

''' Function TODO '''
def view_in_file():
    pass

''' Function to add an account '''
def add_account():
    try:
        enter_account_info()
        display_file_options()
        select_file()
        store_in_file()

    except KeyboardInterrupt:
        program_exit("\n\nKeyboardInterrupt")

''' Function to view accounts '''
def view_accounts():
    try:
        print("\n----- VIEW ACCOUNTS -----\n")
        select_file()
        view_in_file()
    
    except KeyboardInterrupt:
        program_exit("\n\nKeyboardInterrupt")

''' Function to navigate Password Manager menu based on selected option '''
def select_continue(selected_option):
    if selected_option == 1:
        add_account()
    
    elif selected_option == 2:
        view_accounts()
   
    elif selected_option == 3:
        program_exit("\nExit program selected")
    
    else:
        print("\nInvalid option. Try again.")

''' Function main '''
def main():
    while True:
        try:
            display_menu()
            selected_option = menu_select()
            select_continue(selected_option)

        except KeyboardInterrupt:
            program_exit("\n\nKeyboardInterrupt")

''' Call main '''
if __name__ == "__main__":
    main()
