# It's not smart to use this script alone, but it's fine and won't delete your backups, don't worry.
# This will restore your config and personas
# If you want to backup, run backup.py
import os
import shutil
print("Warning: This will delete all your data and replace it with the latest backup.")
print("Would you like to backup your current data before restoring? (y/n)")
confirm = input("")
if confirm == "y":
    os.system("python backup.py")
print("Are you sure you want to restore your backup? (y/n)")
confirm = input("")
if confirm == "y":
    if os.path.exists("./.tmp"):
        print("It seems like your previous restore failed. Deleting .tmp.")
        shutil.rmtree("./.tmp")
    os.mkdir("./.tmp")
    shutil.copytree("./.config/backups", "./.tmp/oldBackups")
    os.mkdir("./.tmp/backup")
    # find most recent backup based on creation date, not name
    backups = os.listdir("./.tmp/oldBackups")
    mostRecentBackup = None
    for backup in backups:
        if mostRecentBackup == None:
            mostRecentBackup = backup
        else:
            creationDate = os.path.getctime("./.tmp/oldBackups/" + backup)
            if creationDate > os.path.getctime("./.tmp/oldBackups/" + mostRecentBackup):
                mostRecentBackup = backup
    shutil.unpack_archive("./.tmp/oldBackups/" + mostRecentBackup, "./.tmp/backup")
    shutil.rmtree("./.config")
    shutil.rmtree("./.personas")
    shutil.rmtree("./.conversations")
    shutil.copytree("./.tmp/backup/.config", "./.config")
    shutil.copytree("./.tmp/backup/.personas", "./.personas")
    shutil.copytree("./.tmp/backup/.conversations", "./.conversations")
    os.mkdir("./.config/backups")
    for backup in backups:
        shutil.copy("./.tmp/oldBackups/" + backup, "./.config/backups")
    shutil.rmtree("./.tmp")
    print("Restore complete.")
else:
    print("Cancelled.")