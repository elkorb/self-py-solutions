def count_chars(my_str):
    my_dict = {}
    for e in "".join(my_str.split()):
        if e in my_dict.keys():
            my_dict[e]+=1
        else:
            my_dict[e] = 1
    return my_dict