from filehandler import display_file_options, select_file, view_in_file

''' Function to view accounts '''
def view_accounts():
    display_file_options()
    file_name, file_path = select_file("view")
    print(f"\n\n\n---------- VIEWING ACCOUNTS IN '{file_name}' ----------\n")
    print("Format: [header] [email] [username] [password]\n")
    view_in_file(file_name, file_path)