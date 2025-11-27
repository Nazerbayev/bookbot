import sys
from stats import get_num_words, get_num_letters, get_sorted_elements


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    [_, path] = sys.argv
    
    text = get_book_text(path)
    
    num_words = get_num_words(text)

    num_letters = get_num_letters(text)

    sorted_elements = get_sorted_elements(num_letters)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    
    print("----------- Word Count ----------")

    print(f"Found {num_words} total words")
    
    print("--------- Character Count -------")

    for el in sorted_elements:
        print(f"{el['char']}: {el['num']}")

    print("============= END ===============")


main()
