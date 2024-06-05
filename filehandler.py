import os
from exithandler import program_exit

''' Function to display the file options '''
def display_file_options():
    print("\n\n\n---------- ACCOUNT FILE OPTIONS ----------\n")
    print("\tcsuf - accounts_csuf.txt")
    print("\tjob - accounts_job.txt")
    print("\tsoftware - accounts_software.txt")
    print("\n------------------------------------------\n")

''' Function to select the file to add account entry to '''
def select_file(message):
    file_name = input(f">\tEnter name of a file to {message}: ")
    valid_file_names = ["csuf", "job", "software"]
    
    if file_name not in valid_file_names:
        program_exit("Invalid file name")
    
    else:
        file_name = "accounts_" + file_name + ".txt"
        file_path = os.path.join("C:/accounts/", file_name)
        print(f"\nChosen file: {file_name}")
        return file_name, file_path

''' Function to see if a header already exists in specified file '''
def check_header_in_file(file_path, header):
    header_arr = []
    file_read = open(file_path, "r")

    for accounts in file_read:
        account_header = accounts.strip().split(" ")[0]
        header_arr.append(account_header)

    file_read.close()

    if header in header_arr:
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

''' Function to view accounts in specified file '''
def view_in_file(file_name, file_path):
    index = 0
    file_read = open(file_path, "r")
    accounts = file_read.readlines()

    for account in accounts:
        index += 1
        print("{}. {}\n".format(index, account.strip()))
        
    file_read.close()