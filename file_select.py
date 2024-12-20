import readline
from os import chdir, getcwd, listdir, path


def file_selector(string: str, dir_color="\033[1;94m"):
    dire = path
    while True:
        strin = string.replace("%%", "%").replace("%P", getcwd())
        user = input(strin)
        hello = user.split()
        if not hello:
            continue
        command = hello[0]
        if command != "ls":
            command_input = hello[1]
        if command == "choose":
            file_name = command_input
            if file_name in listdir() and dire.isfile(file_name):
                return f"{getcwd()}/{file_name}"
            print("\033[31mError: file doesn't exist or is a directory")
        elif command == "ls":
            for file in listdir():
                if dire.isdir(file):
                    print(dir_color + file + "\033[0m")
                    continue
                print(file)
        elif command == "cd":
            if dire.isdir(command_input) or command_input == "..":
                chdir(command_input)
            strin = string
        elif command.lower() in ["q", "quit", "exit", "ex"]:
            quit(0)
        elif command.lower() in ["c", "clear", "cls"]:
            print("\033[H\033[2J\033[3J")
