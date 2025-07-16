print("! Warning !")
print("This script will delete all of your configs and personas. The only purpose of this script is to clean up the folder for normal use.")
print("Type 'y' to confirm.")
print("Type 'n' to cancel.")
print("Type 'a' to keep overrideApiKey.txt.")
confirm = input("Confirm (y/n/a): ")
if confirm == "y" or confirm == "a":
    print("Deleting...")
    import os
    import shutil
    if os.path.exists("./.config/"):
        shutil.rmtree("./.config/")
    if os.path.exists("./.personas/"):
        shutil.rmtree("./.personas/")
    if os.path.exists("./.conversations/"):
        shutil.rmtree("./.conversations/")
    if os.path.exists("./.tmp/"):
        shutil.rmtree("./.tmp/")
    if os.path.exists("./overrideApiKey.txt") and confirm != "a":
        os.remove("./overrideApiKey.txt")
elif confirm == "n":
    print("Cancelled.")