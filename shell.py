# import datetime
import os
import platform

home_dir = os.environ["HOME"]

print("Welcome to vsh! This is an \033[1;37m extremely\033[0m basic shell made with Python." + \
      "\nLast login was on ")


while True:
    current_dir = os.getcwd()
    if home_dir in current_dir:
        current_dir = current_dir.replace(home_dir, "~")
    prompt = f"\033[1;34m{os.getlogin()}\033[0m\033[1;37m@\033[0m\033[1;32m{platform.node()}\033[0m: \033[0;94m{current_dir}\033[0m # "
    cmd = input(prompt)
    if cmd.strip() == "exit":
        with open("last_login.txt", "w") as file:
            # file.write(str(datetime.datetime.now()))
            file.close()
        break
    if cmd.strip().split(" ")[0] == "cd":
        dir = cmd.strip()[3:]
        os.chdir(dir)
        continue
    if cmd.strip() != "":
        output = os.popen(cmd).read()
        print(output, end="")

