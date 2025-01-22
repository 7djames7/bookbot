raw_book = ""
all_words = []
word_count = None
file_path = ""
character_count = {}
character_list = []
alpha_characters = {}

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

def convert_to_list(dict):
    global character_list
    temp_dict={}

    for key in dict:
        temp_dict={}
        temp_dict[key] = dict[key]
        character_list.append(temp_dict) 

def get_dict_value(dict):
  return next(iter(dict.values()))

def sort_and_convert(list):
    temp_dict= {}

    list.sort(reverse=True, key=get_dict_value)
    for dict in list:
        temp_dict.update(dict)

    return temp_dict

def keep_alpha(dict):
    global alpha_characters

    for key in dict:
        if key.isalpha():
            alpha_characters[key] = dict[key]


def main():
    global character_count
    file_path = "books/frankenstein.txt"

    load_book(file_path)
    get_words()
    print(f"The total number off words in the book is:{word_count}")
    get_characters()
    convert_to_list(character_count)
    character_count= sort_and_convert(character_list)
    keep_alpha(character_count)
    for char, amount in alpha_characters.items():
        print(f"The '{char}' character was found {amount} times.")
    
    
    
    
main()