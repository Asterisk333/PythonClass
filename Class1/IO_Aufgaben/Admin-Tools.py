import os

validInputs = ["cwd", "cd", "ls"]


def validate_text_input(input):
    if input.lower() in validInputs:
        return 1


def current_directory():
    print(f"Current Directory: {os.getcwd()}")


def change_directory(path):
    if path == '.':
        # current directory
        pass
    elif path == '..':
        # parent directory
        os.chdir('..')
    elif os.path.isdir(path):
        # specified directory
        os.chdir(path)
    else:
        print(f"Error: The path '{path}' is not a directory.")


def list_contents(pattern=''):
    contents = os.listdir('.')
    for content in contents:
        if content.endswith(pattern):
            print(content)


def run_terminal():
    userinput = ""
    os.system('cls')
    print("Welcome to the Python Admin-Tools")
    while userinput != 'exit':
        userinput = input(">>>")
        if validate_text_input(userinput):
            if userinput.__contains__(' '):
                userinput, additional = userinput.split(' ', 1)
            else:
                additional = ''
                if userinput == 'cwd':
                    current_directory()
                elif userinput == 'cd':
                    change_directory(additional)
                elif userinput == 'ls':
                    list_contents(additional)
        else:
            print("Invalid Input")


run_terminal()
