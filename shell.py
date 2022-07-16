# import datetime
import os
import platform

home_dir = os.environ["HOME"]

print("Welcome to vsh! This is an \033[1;37m extremely\033[0m basic shell made with Python." + \
      "\nLast login was on ")

reset = "\033[0m"
bold_blue = "\033[1;34m"
bold_white = "\033[1;37m"
bold_green = "\033[1;32m"
blue = "\033[0;94m"

while True:
    # get the current working directory
    current_dir = os.getcwd()

    # replace /home/$USER with '~' like in all terminals
    if home_dir in current_dir:
        current_dir = current_dir.replace(home_dir, "~")

    # the main prompt
    prompt = f"{bold_blue}{os.getlogin()}{reset}{bold_white}@{reset}{bold_green}{platform.node()}{reset}{bold_white}:{reset} {blue}{current_dir}{reset} {bold_white}>{reset} "

    cmd = input(prompt)

    # exit the program if user enters 'exit'
    if cmd.strip() == "exit":
        with open("last_login.txt", "w") as file:
            # file.write(str(datetime.datetime.now()))
            file.close()
            os.unlink("last_login.txt")
        break

    # handle cd. os.chdir must be used to change directory. os.system("cd {directory}") doesn't work
    if cmd.strip().split(" ")[0] == "cd":
        dir = cmd.strip()[3:]
        try:
            os.chdir(dir)
        except FileNotFoundError as e:
            print(f"cd: {e.filename}: No such file or directory")
        continue

    # execute the command entered
    if cmd.strip() != "":
        output = os.popen(cmd).read()
        print(output, end="")

