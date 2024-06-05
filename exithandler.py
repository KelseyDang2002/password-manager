import time

''' Function to handle program exits '''
def program_exit(message):
    print(f"\n\n{message} -> Program exiting...")
    time.sleep(1)
    print("Goodbye.")
    exit(0)