raw_book = ""
all_words = []
word_count = None
file_path = ""
character_count = {}

def load_book(path):
    global raw_book
    with open(path) as f:
        raw_book = f.read()


def get_words():
    global all_words
    global word_count

    all_words = raw_book.split()
    word_count = len(all_words)

def get_characters():
    global character_count
    book_lowercase = raw_book.lower()

    for char in book_lowercase:
        character_count[char]= character_count.get(char, 0)+1


def main():
    file_path = "books/frankenstein.txt"

    load_book(file_path)
    get_words()
    get_characters()
    
    print(f"The total number off words in the book is:{word_count}")
    print(f"Here is a list of all the characters and there counts:{character_count}")

    
main()