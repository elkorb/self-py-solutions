def numbers_letters_count(my_str):
    digits = 0
    letters = 0

    for item in my_str:
        letters+=1
        if item.isdigit():
            digits += 1
    return [digits,letters-digits]