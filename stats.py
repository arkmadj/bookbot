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
        if not char.isalpha():
            continue
        if char.lower() not in count_dict:
            count_dict[char.lower()] = 1
        else:
            count_dict[char.lower()] += 1

    return count_dict
    
def sort_on(count: tuple[str, int]) -> int:
    return count[1]

def chars_dict_to_sorted_list(counts: dict[str, int]) -> list[tuple[str, int]]:
    count_list: list[tuple[str, int]] = []
    for char in counts:
        count = counts[char]
        count_list.append((char, count))
    return sorted(count_list, reverse=True, key=sort_on)
