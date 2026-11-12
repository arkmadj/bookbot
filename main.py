from stats import get_num_words

def main():
    file_path = "./books/frankenstein.txt"
    print(f"Found {get_num_words(file_path)} total words")

main()
