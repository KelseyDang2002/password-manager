from add import add_account
from view import view_accounts
from exithandler import program_exit

''' Function to display Password Manager menu '''
def display_menu():
    print("\n\n\n__________ PASSWORD MANAGER MENU __________")
    print("|                                         |")
    print("|\tadd - Add an account              |")
    print("|\tview - View accounts              |")
    print("|\texit - Exit program               |")
    print("___________________________________________\n")

''' Function to select menu option '''
def menu_select():
    selected_option = input(">\tSelect a menu option: ")
    print(f"\nYou entered option '{selected_option}'.")
    
    if selected_option == "add":
        add_account()
    elif selected_option == "view":
        view_accounts()
    elif selected_option == "exit":
        program_exit("Exit program selected")
    else:
        print(f"\nInvalid command '{selected_option}'. Try again.")

''' Driver '''
if __name__ == "__main__":
    while True:
        try:
            display_menu()
            menu_select()

        except KeyboardInterrupt:
            program_exit("\nKeyboardInterrupt")
