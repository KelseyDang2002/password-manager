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
import pwinput

def program_exit(error):
    print(error, "-> Program exiting...")
    time.sleep(1)
    print("Goodbye.")
    exit(0)

def select_file():
    file_name = input("Enter the filename to append account to: ")
    file_path = ""
    return file_path

def read_file(file_path):
    pass

def append_to_file(file_path):
    file_path = select_file()
    file_append = open(file_path, "a")

def store_in_file():
    pass

def display_menu():
    print("\n----- PASSWORD MANAGER MENU -----\n")
    print("->\t1. Add an account")
    print("->\t2. View accounts")
    print("->\t3. Exit program")
    print("\n---------------------------------\n")

def menu_select():
    selected_option = int(input("Select a menu option: "))
    print("You entered option", selected_option)
    return selected_option

def select_continue(selected_option):
    if selected_option == 1:
        header, email, username, password = add_account()
        store_in_file()
    
    elif selected_option == 2:
        view_accounts()
   
    elif selected_option == 3:
        program_exit("\nExit program selected")
    
    else:
        print("\nInvalid option. Try again.")

def add_account():
    try:
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
    
    except KeyboardInterrupt:
        program_exit("\n\nKeyboardInterrupt")

def view_accounts():
    try:
        print("\n----- VIEW ACCOUNTS -----\n")
    
    except KeyboardInterrupt:
        program_exit("\n\nKeyboardInterrupt")

def main():
    while True:
        try:
            display_menu()
            selected_option = menu_select()
            select_continue(selected_option)

        except KeyboardInterrupt:
            program_exit("\n\nKeyboardInterrupt")

if __name__ == "__main__":
    main()
