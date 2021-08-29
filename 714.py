def squared_numbers(start, stop):
    list = []
    i = start
    while i <= stop:
        list.append(i**2)
        i+=1
    return list