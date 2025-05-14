from stats import get_num_words, get_num_chars, sorted_dict_list
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_text = f.read()
        return file_text

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}")
        print("----------- Word Count ----------")
        book_contents = get_book_text(f"{book_path}")
        num_words = get_num_words(book_contents)
        print(f"Found {num_words} total words")
        print("--------- Character Count ------")
        num_chars_dict = get_num_chars(book_contents)
        sorted_charcount_list = sorted_dict_list(num_chars_dict)
        for i in range(0,len(sorted_charcount_list)):
            if sorted_charcount_list[i]["char"].isalpha():
                print(f"{sorted_charcount_list[i]["char"]}: {sorted_charcount_list[i]["num"]}")
    return

main()