def sequence_del(my_str):
    if not my_str:
        return ""
    new_str = my_str[0]
    for char in my_str:
        if new_str[-1] != char:
            new_str+=char
    return new_str
