def check_valid_input(letter_guessed, old_letters_guessed):
    if ((len(letter_guessed) > 1) or (not letter_guessed.isalpha()) or (letter_guessed.lower() in old_letters_guessed)):
        return False
    else:
        return True