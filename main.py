from stats import get_num_words, get_book_text, get_chars_count, chars_dict_to_sorted_list

def main():
    file_path = "./books/frankenstein.txt"
    book_contents = get_book_text(file_path)
    print(f"Found {get_num_words(book_contents)} total words")
    char_count = get_chars_count(book_contents)
    print(char_count)
    print(chars_dict_to_sorted_list(char_count))

main()
