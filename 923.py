def who_is_missing(file_name):
    f = open(file_name)
    g = f.read()
    my_list = sorted(list(g.split(",")))
    print(my_list)
    acc = 1
    for item in my_list:
        if int(item) == acc:
            acc+=1
            continue
        else:
            new = open("found.txt",'w')
            new.write(str(acc))
            new.close()
            f.close()
            return acc
    f.close()