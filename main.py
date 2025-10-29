from stats import get_num_words, char_count, get_sorted_dicts
import sys

#get the book text from file
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    #check if sys doesn't have arguments
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_book = sys.argv[1]
    book_text = get_book_text(path_to_book)
    total_words = get_num_words(book_text)
    char_dict = char_count(book_text)
    dict_list = get_sorted_dicts(char_dict)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for d in dict_list:
        if not d["char"].isalpha():
            continue
        print(f"{d['char']}: {d['num']}")
main()