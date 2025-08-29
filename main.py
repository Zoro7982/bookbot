from stats import count_words,num_words,char_dict_to_sorted_list
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    filepath=sys.argv[1]
    text=get_book_text(filepath)
    word_count=count_words(text)
    char_dict=num_words(text)
    char_sorted_list=char_dict_to_sorted_list(char_dict)
    print_report(filepath,word_count,char_sorted_list)

def get_book_text(filepath):
    with open(filepath) as f:
        text=f.read()
    return text

def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")
main()