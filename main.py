def main():
    filepath="books/frankenstein.txt"
    text=get_book_text(filepath)
    return print(f"{count_words(text)} words found in the document")

def get_book_text(filepath):
    with open(filepath) as f:
        text=f.read()
    return text

def count_words(text):
    word=text.split()
    return len(word)

main()