my_path = input("Enter file path:")
action_name = input("Enter action name (sort, rev or last):")

with open(my_path, 'r') as file_c:
    if (action_name == "sort"):
        a = file_c.read().replace("\n"," ").split(" ")
        b = sorted(list(dict.fromkeys(a)))
        print(b[1:])
    elif (action_name == "rev"):
         for line in file_c:
             print(line[-1::-1])
    elif (action_name == "last"):
        n = int(input("Enter number:"))
        lines = file_c.readlines()
        print('\n'.join(lines[n:]))

