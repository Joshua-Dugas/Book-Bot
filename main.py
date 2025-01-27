#Globals
frank_path = 'books/frankenstein.txt'

def main():
    with open(frank_path) as f:
        file_contents = f.read(-1)
    book_words = file_contents.split()
    
#Functions Calls
    word_count(book_words)
    char_dict = char_count(file_contents)
    print_book_report(char_dict)

#Functions
def word_count(book_word_list):
    return word_count

def char_count(book_raw):
    lower_case_book_raw = book_raw.lower()
    char_dict = {}
    for char in lower_case_book_raw:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    for entry in char_dict:
        char_int = char_dict[entry]
        #print(f"The '{entry}' character was found {char_int} times")
    return  char_dict

def print_book_report(char_dict):
    dict_list = []
    #Convert dict to list of dicts to prepare it for sorting
    for entry in char_dict:
        char_int = char_dict[entry]
        temp_dict = {"letter": entry, "Count": char_int}
        dict_list.append(temp_dict)
    #This takes the list of dicts and sorts them by the 'count' key in reverse
    sorted_char_dict = sorted(dict_list, reverse=True, key=lambda d: d ['Count'])

    print("-----------Begin Report-----------")
    for entry in dict_list:
        if entry["letter"].isalpha():
            print(f"The '{entry["letter"]}' character was found  {entry["Count"]} times")
    print("-----------End Report-----------")
def sort_on(char_dict):
    return char_dict["Count"]


if __name__ == "__main__":
    main()

