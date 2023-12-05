
def read_file(file_path):
    file_name = file_path.split('/')[-1].split('_')[0]
    with open(file_path, 'r', encoding="utf-8") as file:
        file_content = file.read()
    return file_name, file_content
