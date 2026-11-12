def get_book_text(path: str) -> str:
    file_contents: str
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def get_num_words(text: str) -> int:
    return len(text.split())

def get_chars_count(text) -> dict[str, int]:
    count_dict: dict[str, int] = {}
    for char in text:
        if char.lower() not in count_dict:
            count_dict[char.lower()] = 1
        else:
            count_dict[char.lower()] += 1

    return count_dict
    

