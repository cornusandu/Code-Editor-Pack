from colorama import Fore
import os

os.system("cls")

file = input("Type in the file name\n> ")
dir = f"dir_{file}__edited"
try:
    os.mkdir(dir)
    filelocation = f"{dir}\\{file}"
except:
    if dir != '':
        filelocation = f"{dir}\\{file}"
    else:
        filelocation = file

command = input(f"Chose an edit type.\n\n{Fore.BLUE}UPPERCASE\nlowercase\nno numbers\nbase64encoded\nbase64decoded{Fore.RESET}\n\n> ")
commands = list("uppercase;lowercase;no numbers;base64encoded;base64decoded".split(";"))

if not command.lower() in commands:
    print(f"{Fore.RED}That is not a valid command!{Fore.RESET}")
    exit(1)

elif command.lower() == commands[0]:
    with open(file, "r") as f:
        lines = list(f.read().split("\n"))
    try:
        nfilelocation = f"{dir}\\{file.upper()}"
    except:
        nfilelocation = file.upper()
    with open(nfilelocation, "w") as f:
        for i in lines:
            f.write(i.upper())
            f.write("\n")

elif command.lower() == commands[1]:
    with open(file, "r") as f:
        lines = list(f.read().split("\n"))
    try:
        nfilelocation = f"{dir}\\{file.lower()}__lower"
    except:
        nfilelocation = file.lower()
    with open(nfilelocation, "w") as f:
        for i in lines:
            f.write(i.lower())
            f.write("\n")

elif command.lower() == commands[2]:
    with open(file, "r") as f:
        lines = list(f.read().split("\n"))
    try:
        nfilelocation = dir + "\\" + file + "_nonr"
    except:
        nfilelocation = file + "_nonr"
    numbers = list(range(0, 10))
    with open(nfilelocation, "w") as f:
        for line in lines:
            for char in line:
                try:
                    if int(char) in numbers:
                        pass
                    else:
                        f.write(char)
                except:
                    f.write(char)
            f.write("\n")

elif command.lower() == commands[3]:
    from base64 import b64encode
    with open(file, "r") as f:
        lines = list(f.read().split("\n"))
    try:
        nfilelocation = f"{dir}\\{b64encode(file.encode())}"
    except:
        nfilelocation = f"{b64encode(file.encode())}"
    with open(nfilelocation, "w") as f:
        for i in lines:
            i = i.encode()
            i = b64encode(i)
            i = i.decode()
            f.write(i)
            f.write("\n")
elif command.lower() == commands[4]:
    from base64 import b64decode
    with open(file, "r") as f:
        lines = list(f.read().split("\n"))
    nfilelocation = b''
    try:
        nfilelocation = f"{dir}\\{b64decode(file.encode())}"
    except:
        nfilelocation = f"{b64decode(file.encode())}"
    with open(nfilelocation, "w") as f:
        for i in lines:
            i = i.encode()
            i = b64decode(i)
            i = i.decode()
            f.write(i)
            f.write("\n")