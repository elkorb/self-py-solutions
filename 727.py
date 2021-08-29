def arrow(my_char, max_length):
    str=""
    for i in range(max_length):
        str+=(((my_char) * (i+1)) + '\n')
    for i in range(max_length,1,-1):
        str+= ((my_char)  * (i-1)) + '\n'
    return str[:-1]