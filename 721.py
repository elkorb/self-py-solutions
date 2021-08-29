def is_greater(my_list, n):
    new_list = []
    for item in my_list:
        if item > n:
            new_list.append(item)
    return new_list