def shift_left(my_list):
    a = my_list[0]
    my_list[0] = my_list[1]
    my_list[1] = my_list[2]
    my_list[2] = a
    return my_list