
def main():
    path = "books/frankenstein.txt"
    print(f"--- Begin report of {path} ---")
    
    book_data = read_book_text(path)
    book_word_length = word_text_length(book_data)
    print(f"{book_word_length} words found in the document")
    
    char_count = count_characters(book_data)
    for character in char_count:
        print(f"The '{character['value']}' character was found {character['count']} times")
    
    print("--- End report ---")

def read_book_text(path):
    with open(path) as f:
        return f.read()

def word_text_length(words):
    return len(words.split())

def sort_on(dict):
    return dict["count"]

def count_characters(words):
    char_dict = {i : 0 for i in list(map(chr, range(97, 123)))}
    #chars = {}
    for char in words.lower():
        if char in char_dict:
            char_dict[char] += 1
            
    #convert to individual dict
    char_list = [{"value" : i , "count" : k } for i ,k in char_dict.items() ]
    char_list.sort(reverse=True, key=sort_on)
    return char_list

main()
