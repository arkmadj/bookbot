from stats import get_num_words, get_book_text, get_chars_count

def main():
    file_path = "./books/frankenstein.txt"
    book_contents = get_book_text(file_path)
    print(f"Found {get_num_words(book_contents)} total words")
    print(get_chars_count(book_contents))
main()
