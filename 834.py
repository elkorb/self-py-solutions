def inverse_dict(my_dict):
    inversed = {}
    for key in my_dict:
            if my_dict[key]  not in  inversed:
                inversed[ my_dict[key]] = [key]
            else:
                inversed[my_dict[key]].append(key)
                inversed[my_dict[key]].sort()
    return inversed
