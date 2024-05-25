'''
Password Manager Structure

Core Features:
1. Add account entry to txt file
    - Account Entry Format: <header> : <email> <username> <password>
    - <header> = header name of the account (i.e. Gmail Account)
    - <email> = email of account
    - <username> = username of account
    - <password> = password of account
    - Separate each entry with an empty line
2. Edit passwords of existing account?
3. Salt passwords and hash passwords?
4. Password generator
    - Arguments: keywords
'''

import time
import os
import pwinput

''' Function to display Password Manager menu '''
def display_menu():
    print("\n\n\n__________ PASSWORD MANAGER MENU __________\n")
    print("\tadd - Add an account")
    print("\tview - View accounts")
    print("\texit - Exit program")
    print("\n___________________________________________\n")

''' Function to select menu option '''
def menu_select():
    selected_option = input(">\tSelect a menu option: ")
    print(f"\nYou entered option '{selected_option}'.")
    return selected_option

''' Function to enter account information '''
def enter_account_info():
    print("Type 'none' if email or username is not applicable.\n")
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
    
    # print(f"\nYou entered: {header} {email} {username} {password}")
    print(f"\nYou entered:")
    print(f"\tHeader:\t\t{header}")
    print(f"\tEmail:\t\t{email}")
    print(f"\tUsername:\t{username}")
    print(f"\tPassword:\t{password}")
    return header, email, username, password

''' Function to display the file options '''
def display_file_options():
    print("\n\n\n---------- ACCOUNT FILE OPTIONS ----------\n")
    print("\taccounts_csuf.txt")
    print("\taccounts_job.txt")
    print("\taccounts_software.txt")
    print("\n------------------------------------------\n")

''' Function to select the file to add account entry to '''
def select_file(message):
    file_name = input(f">\tEnter name of a file to {message} (csuf, job, software): ")
    valid_file_names = ["csuf", "job", "software"]
    
    if file_name not in valid_file_names:
        program_exit("Invalid file name")
    
    else:
        file_name = "accounts_" + file_name + ".txt"
        file_path = os.path.join("C:/accounts/", file_name)
        print(f"\nChosen file: {file_name}")
        return file_name, file_path

''' Function to file to see if a header already exists '''
def check_header_in_file(file_path, header):
    header_arr = []
    file_read = open(file_path, "r")

    for accounts in file_read:
        account_header = accounts.strip().split(" ")[0]
        header_arr.append(account_header)

    file_read.close()

    if header in header_arr:
        print(header_arr)
        return False
    else:
        return True
    
''' Function to store account entry in the file '''
def store_in_file(file_name, file_path, header, email, username, password):
    header_is_valid = check_header_in_file(file_path, header)

    if header_is_valid == False:
        program_exit(f"Entry denied, account for {header} already exists")
    
    else:
        account = header + " " + email + " " + username + " " + password
        print(f"\nAccount entry: {account}")
        file_append = open(file_path, "a")
        file_append.write("{}\n".format(account))
        file_append.close()
        print(f"Account entry successfully added to '{file_name}'!")

''' Function TODO '''
def view_in_file(file_name, file_path):
    index = 0
    file_read = open(file_path, "r")
    accounts = file_read.readlines()

    for account in accounts:
        index += 1
        print("{}. {}\n".format(index, account.strip()))
        
    file_read.close()

''' Function to add an account '''
def add_account():
    display_file_options()
    file_name, file_path = select_file("add account to")
    print(f"\n\n\n---------- ADDING ACCOUNT TO '{file_name}' ----------\n")
    header, email, username, password = enter_account_info()
    store_in_file(file_name, file_path, header, email, username, password)

''' Function to view accounts '''
def view_accounts():
    display_file_options()
    file_name, file_path = select_file("view")
    print(f"\n\n\n---------- VIEWING ACCOUNTS IN '{file_name}' ----------\n")
    print("Format: [header] [email] [username] [password]\n")
    view_in_file(file_name, file_path)
    
''' Function to handle program exits '''
def program_exit(message):
    print(f"\n\n{message} -> Program exiting...")
    time.sleep(1)
    print("Goodbye.")
    exit(0)

''' Function to navigate Password Manager menu based on selected option '''
def select_continue(selected_option):
    if selected_option == "add":
        add_account()
    elif selected_option == "view":
        view_accounts()
    elif selected_option == "exit":
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
