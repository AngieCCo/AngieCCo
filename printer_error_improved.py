def printer_errors(s):

    good_letters = "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"
    count_letters = 0
    count_total = len(s)

    for letter in s:
        its_good_letter = None
        for good_letter in good_letters:
            if good_letter == letter:
                its_good_letter = True
        if its_good_letter is None:
            its_good_letter = False

        if its_good_letter:
            count_letters += 0
        else:
            count_letters += 1

    result = f"{count_letters}/{count_total}"

    return result

print(printer_errors("kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyzuuuuu"))