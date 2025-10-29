#get the total number of words
def get_num_words(book_text):
    word_list = book_text.split()
    return len(word_list)

#count amount of times char appears
def char_count(book_text):
    char_dict = {}
    for c in book_text:
        c = c.lower()
        char_dict[c] = 1 + char_dict.get(c, 0)
    return char_dict

#get sorted list of dicts
def get_sorted_dicts(char_dict):
    dict_list = []
    for k,v in char_dict.items():
        curr = {}
        curr["char"] = k
        curr["num"] = v
        dict_list.append(curr)
    dict_list.sort(key=lambda d: d["num"], reverse=True)
    return dict_list