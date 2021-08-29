def check_win(secret_word, old_letters_guessed):
    for i in secret_word:
        if not i in old_letters_guessed:
            return False 
    return True