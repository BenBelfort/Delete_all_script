# IMPORTS
import os

# GLOBALS
YES = 'y'
NO = 'n'

# FUNCTIONS
def ask_again() -> int:
    answer = input("You want to delete files in another directory (Y/N)? > ").lower()
    if answer == NO:
        return 0
    elif answer == YES:
        return 1
    else:
        return 2

def delete_all_files(path) -> bool:
    if os.path.exists(path):
        for filename in os.listdir(path):
            file_path = os.path.join(path,filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Deleted {filename} in {file_path}")
        print("All files have been deleted")
        return True
    else:
        print("The path you entered does not exist in your local system")
        return False

def main_function() -> int:
    path = input("Please enter the path to the directory you want to delete all files in > ")
    if not isinstance(path, str):
        print("Please enter a string...")
        return 1

    print("--Trying to delete all files--")
    success = delete_all_files(path)

    if success:
        print("All files have successfully been deleted.")
    else:
        print("[Error] Something went wrong while trying to delete your files.")
        return 2

if __name__ == '__main__':
    repeat = 1              # initilize with 1 to start the loop
    first_in = True         # needs to be True as a "flag" for the first entrance
    error_in_main = 0       # value for the specific error in the main function

    print("--Starting script")
    while repeat:
        error_in_main = main_function()
        if error_in_main == 1:
            error_in_main = 0
            continue
        elif error_in_main == 2:
            error_in_main = 0
            print("Maybe try to check the given path")

        while repeat == 2 or first_in:
            first_in = False
            repeat = ask_again()

        first_in = True

    print("--Shutting down--")
