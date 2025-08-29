from stats import count_words
from stats import num_words
def main():
    filepath="books/frankenstein.txt"
    text=get_book_text(filepath)
    return print(f"{count_words(text)} words found in the document"),print(num_words(text))

def get_book_text(filepath):
    with open(filepath) as f:
        text=f.read()
    return text

main()