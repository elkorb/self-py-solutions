def mult_tuple(tuple1, tuple2):
    t_list = []
    for element1 in tuple1:
        for element2 in tuple2:
            t_list.append((element1,element2))
            t_list.append((element2,element1))
    return t_list

first_tuple = (1, 2,3) 
second_tuple = (4, 5,6)
print(mult_tuple(first_tuple, second_tuple))