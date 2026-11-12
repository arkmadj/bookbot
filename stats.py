def get_num_words(path):
    file_contents = ""
    with open(path) as f:
        file_contents = f.read()
    return len(file_contents.split())

