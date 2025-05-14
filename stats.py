def get_num_words(text_string):
    word_list = text_string.split()
    num_words = len(word_list)
    return num_words

def get_num_chars(text_string):
    lower_converted_string = text_string.lower()
    list_chars = list(lower_converted_string)
    dict_char = {}
    for i in range(0,len(list_chars)):
        if list_chars[i] in dict_char:
            dict_char[list_chars[i]] = dict_char[list_chars[i]] + 1
        else:
            dict_char[list_chars[i]] = 1
    return dict_char          

def sort_on(dict):
    return dict["num"] 

def sorted_dict_list(dict_chars):
    sorted_list = []
    for char in dict_chars:
        char_num_dict = {
            "char": char,
            "num": dict_chars[char]
        }
        sorted_list.append(char_num_dict)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

