def check_valid_input(letter_guessed, old_letters_guessed):
    if ((len(letter_guessed) > 1) or (not letter_guessed.isalpha()) or (letter_guessed.lower() in old_letters_guessed)):
        return False
    else:
        return True

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if check_valid_input(letter_guessed,old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        print("X")
        print(" -> ".join(sorted(old_letters_guessed)))
        return False