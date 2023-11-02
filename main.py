# IMPORTS
import os

# FUNCTIONS
def delete_all_files(path):
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

if __name__ == '__main__':

    path = input("Please enter the path to the directory you want to delete all files in > ")
    if not isinstance(path,str):
        print("Please enter a string...")
        exit(1)

    print("--Trying to delete all files--")

    success = delete_all_files(path)

    if success:
        print("All files have successfully been deleted.")
    else:
        print("[Error] Something went wrong while trying to delete your files.")