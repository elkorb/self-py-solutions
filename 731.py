def show_hidden_word(secret_word, old_letters_guessed):
    new_string = ""
    for i in range(len(secret_word)):
        if secret_word[i] in old_letters_guessed:
            new_string+=secret_word[i] + " "
        else:
            new_string+='_ '
    return new_string[:-1]
        