def read_file(file_name):
    try:
        with open(file_name, 'r') as f:
            content = f.read()
            return content
    except FileNotFoundError:
        return "File Not Found"


def write_file(file_name, content):
    with open(file_name, 'w') as f:
        f.write(content)
        return "Done, file saved successfully"
