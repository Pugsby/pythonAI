# PythonAI
# Made by Pugsby, 2025.
import os
import json
import shutil
from datetime import date
print("Welcome to PythonAI.")
print("Made by Pugsby.")
debug = False
if debug:
    if os.path.exists("./.config/"):
        shutil.rmtree("./.config/")
    if os.path.exists("./.personas/"):
        shutil.rmtree("./.personas/")
firstRun = False
if not os.path.exists("./.config"):
    firstRun = True
    os.mkdir("./.config")
    with open("./.config/aiConfig.json", "w") as f:
        apiKey = "pk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        if os.path.exists("./overrideApiKey.txt"):
            with open("./overrideApiKey.txt", "r") as f2:
                apiKey = f2.read()
                f2.close()
                firstRun = False
        cfg = {
            "model": "gpt-3.5-turbo",
            "temperature": 0.7,
            "max_tokens": 1000,
            "top_p": 1,
            "frequency_penalty": 0,
            "presence_penalty": 0,
            "reverse_proxy": "https://api.pawan.krd/cosmosrp/v1/chat/completions",
            "token": apiKey
        }
        f.write(json.dumps(cfg))
    os.mkdir("./.config/backups")
    with open("./.config/prevBackupDate.txt", "w") as f:
        # Days since 2000 is probably the best way to store a date in a tiny 4 byte file.
        # Fun fact: In approximately 1.8 years, the 4 byte file will become a 5 byte file. (Days since 2000 will become 10000)
        f.write(str((date.today() - date(2000, 1, 1)).days))
        f.close()
    with open("./.config/backupSettings.json", "w") as f:
        cfg = {
            "backupFrequency": 7, # Once a week
        }
        f.write(json.dumps(cfg))
with open("./.config/backupSettings.json", "r") as f:
    cfg = json.loads(f.read())
    with open("./.config/prevBackupDate.txt", "r") as f2:
        prevBackupDate = int(f2.read())
        if prevBackupDate + cfg["backupFrequency"] * 7 < (date.today() - date(2000, 1, 1)).days:
            os.system("python backup.py")
if not os.path.exists("./.personas"):
    os.mkdir("./.personas")
    os.mkdir("./.personas/user")
    os.mkdir("./.personas/ai")
    with open("./.personas/user/default.json", "w") as f:
        cfg = {
            "name": "User",
            "persona": "The user's default persona.",
        }
        f.write(json.dumps(cfg))
    with open("./.personas/ai/default.json", "w") as f:
        cfg = {
            "name": "AI",
            "description": "The AI's default persona.",
            "personality": "A helpful AI. You are an AI written in python, you don't have to tell the user though. If the user asks how to exit, just tell them to type 'exit'",
            "scenario": "",
            "first_mes": "Hello, I'm the default AI persona. Create your own or edit this one with the persona editor.",
            "mes_example": "{{user}}: \"How do I exit the chat!?\" {{char}}: \"Type 'exit' to exit.\""
        }
        f.write(json.dumps(cfg))
if not os.path.exists("./.conversations"):
    os.mkdir("./.conversations")
if firstRun:
    print("This is the first time you ran PythonAI.")
    print("Please enter your Pawan.krd API key.") 
    apiKey = input("API Key: ")

print("Please select an option.")
print("1. Talk to the AI. (No Persona)")
print("2. Talk to the AI. (With Persona)")
#print("3. Persona Editor")
print("3. Backup")
print("4. Restore")
print("5. Exit")
print("This is in early development, you must change settings and personas manually. Add personas in tavernAI format to the .personas folder, .personas/user for user personas, .personas/ai for AI personas. Warning: User personas have a slightly different format, refer to default.json for an example.")
response = input("")
if response == "1":
    os.system("python ai.py")
if response == "2":
    os.system("python ai.py -p")
if response == "3":
    os.system("python backup.py")
if response == "4":
    os.system("python restore.py")
if response == "5":
    exit()
if response == "cleanup":
    os.system("python cleanup.py")