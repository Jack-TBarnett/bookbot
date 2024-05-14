def main():
    book_path = "books/frankenstein.txt"
    text = get_book(book_path)
    word_count = num_words(text)
    letters_dict = get_dict(text)
    letters_sorted = dict_sorted(letters_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()

    for i in letters_sorted:
        if not i["char"].isalpha():
            continue
        print(f"The '{i['char']}' character was found {i['num']} times")

    print("--- End report ---")



def sort_on(dict):
    return dict["num"]


def dict_sorted(letters_dict):
    sorted_list = []
    for lt in letters_dict:
        sorted_list.append({"char": lt, "num": letters_dict[lt]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def get_dict(text):
    letters = {}
    for lets in text:
        lowered = lets.lower()
        if lowered in letters:
            letters[lowered] +=1
        else:
            letters[lowered] = 1
    return letters

def num_words(text):
    words = text.split()
    return len(words)


def get_book(path):
    with open(path) as f:
        return f.read()

main()