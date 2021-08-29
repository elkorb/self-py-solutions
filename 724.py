def seven_boom(end_number):
    new_list = []
    for number in range(end_number+1):
        if ((number % 7 == 0) or ('7' in str(number))):
            new_list.append("BOOM")
        else:
            new_list.append(number)
    return new_list
