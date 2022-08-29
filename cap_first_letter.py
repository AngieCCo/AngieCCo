def to_jaden_case(string):

    # cap_1st_letter = string.title()
    # return cap_1st_letter
    split_words = string.split(" ")
    final_lst = []

    for i in range(len(split_words)):
        word = split_words[i]
        cap_word = word.capitalize()
        final_lst.append(cap_word)

    print(final_lst)
    final_str = " ".join(final_lst)

    return final_str


print(to_jaden_case("the word would be better if everyone plants a tree"))