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
def program_exit(message):
    print(f"\n\n{message} -> Program exiting...")
    time.sleep(1)
    print("Goodbye.")
    exit(0)

''' Function to display Password Manager menu '''
def display_menu():
    print("\n\n__________ PASSWORD MANAGER MENU __________\n")
    print("\t1. Add an account")
    print("\t2. View accounts")
    print("\t3. Exit program")
    print("\n___________________________________________\n")

''' Function to select menu option '''
def menu_select():
    selected_option = int(input(">\tSelect a menu option: "))
    print(f"\nYou entered option {selected_option}.")
    return selected_option

''' Function to enter account information '''
def enter_account_info():
    header = input(">\tName the account header: ")
    email = input(">\tEnter email: ")
    username = input(">\tEnter username: ")
    # password = pwinput.pwinput(prompt="Enter password: ")
    # password_confirm = pwinput.pwinput(prompt="Confirm password: ")
    password = input(">\tEnter password: ")
    password_confirm = input(">\tConfirm password: ")

    if password_confirm != password:
        program_exit("Passwords do not match")
    
    else:
        print(f"\nYou entered: {header} {email} {username} {password}")
        return header, email, username, password

''' Function to display the file options '''
def display_file_options():
    print("\n\n---------- ACCOUNT FILE OPTIONS ----------\n")
    print("\taccounts_csuf.txt")
    print("\taccounts_job.txt")
    print("\taccounts_software.txt")
    print("\n------------------------------------------\n")

''' Function to select the file to add account entry to '''
def select_file():
    file_name = input(">\tEnter name of a file to add account to (csuf, job, software): ")
    valid_file_names = ["csuf", "job", "software"]
    
    if file_name not in valid_file_names:
        program_exit("Invalid file name")
    
    else:
        file_name = "accounts_" + file_name + ".txt"
        file_path = os.path.join("C:/Users/Kelsey PC/Documents/", file_name)
        return file_path

''' Function to file to see if a header already exists '''
def check_header_in_file(file_path, header):
    header_arr = []
    file_read = open(file_path, "r")

    for accounts in file_read:
        header = accounts.strip().split(" ")
        header_arr.append(header)

    file_read.close()

    if header in header_arr:
        return False
    else:
        return True

''' Function to store account entry in the file '''
def store_in_file(file_path, header, email, username, password):
    header_is_valid = check_header_in_file(file_path, header)

    if header_is_valid == False:
        program_exit("Entry denied, account already exists")
    
    else:
        account = header+" "+email+" "+username+" "+password
        print("\nOverview:")
        print(f"Account entry: {account}")
        print(f"File path: {file_path}")
        # file_path = select_file()
        # file_append = open(file_path, "a")
        # file_append.write("{}\n".format(account))

''' Function TODO '''
def view_in_file(file_path):
    pass

''' Function to add an account '''
def add_account():
    print("\n\n---------- ADD AN ACCOUNT ----------\n")
    header, email, username, password = enter_account_info()
    display_file_options()
    file_path = select_file()
    store_in_file(file_path, header, email, username, password)

''' Function to view accounts '''
def view_accounts():
    print("\n\n---------- VIEW ACCOUNTS ----------\n")
    file_path = select_file()
    view_in_file(file_path)

''' Function to navigate Password Manager menu based on selected option '''
def select_continue(selected_option):
    if selected_option == 1:
        add_account()
    elif selected_option == 2:
        view_accounts()
    elif selected_option == 3:
        program_exit("Exit program selected")
    else:
        print("\nInvalid option. Try again.")

''' Driver '''
if __name__ == "__main__":
    while True:
        try:
            display_menu()
            selected_option = menu_select()
            select_continue(selected_option)

        except KeyboardInterrupt:
            program_exit("\nKeyboardInterrupt")
