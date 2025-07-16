# It's not smart to use this script alone, but it's fine and won't delete your backups, don't worry.
# This will backup your config and personas to .config/backups
# If you want to restore from a backup, run restore.py
import os
import shutil
from datetime import date
import random
print("Backing up...")
if os.path.exists("./.tmp"):
    print("It seems like your previous backup failed. Deleting .tmp.")
    shutil.rmtree("./.tmp")
with open("./.config/prevBackupDate.txt", "w") as f:
    f.write(str((date.today() - date(2000, 1, 1)).days))
    f.close()
os.mkdir("./.tmp")
shutil.copytree("./.config", "./.tmp/.config")
shutil.copytree("./.personas", "./.tmp/.personas")
shutil.copytree("./.conversations", "./.tmp/.conversations")
# delete .tmp/.config/backups
if os.path.exists("./.tmp/.config/backups"):
    shutil.rmtree("./.tmp/.config/backups")
shutil.make_archive("./.config/backups/backup-" + str((date.today() - date(2000, 1, 1)).days) + "-" + str(random.randint(10000,99999)), "zip", "./.tmp/")
shutil.rmtree("./.tmp")
print("Backup complete.")