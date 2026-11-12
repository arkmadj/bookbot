def get_book_word_count(path):
    file_contents = ""
    with open(path) as f:
        file_contents = f.read()
    return len(file_contents.split())

def main():
    file_path = "./books/frankenstein.txt"
    print(f"Found {get_book_word_count(file_path)} total words")

main()
