import sys
from stats import get_num_words, get_book_text, get_chars_count, chars_dict_to_sorted_list

def main():
    print("============ BOOKBOT ============")
    file_path = sys.argv[1]
    print(f"Analyzing book found at {file_path}...")
    book_contents = get_book_text(file_path)
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book_contents)} total words")
    print("--------- Character Count -------")
    char_count = get_chars_count(book_contents)
    sorted_char_count = chars_dict_to_sorted_list(char_count)
    for count in sorted_char_count:
        print(f"{count[0]}: {count[1]}")
    print("============= END ===============")

main()
