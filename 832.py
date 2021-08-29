from datetime import datetime
from datetime import date

my_dict = {"first_name":"Mariah", "last_name":" Carey", "birth_date":"27.03.1970","hobbies":"Sing, Compose, Act"}
user_input = int(input("""
1. Print last name.
2. Print birth month.
3. Print hobbies amount.
4. Print last hobbie. 
5. Add \"Cooking\" to hobbies.
6. Make birth date a tuple.
7. Add new \"age\" key with value. 
please enter option:"""))

if user_input == 1:
    print(my_dict["last_name"])
elif user_input == 2:
    print(my_dict["birth_date"][4:6])
elif user_input == 3:
    print(len(my_dict["hobbies"].split(",")))
elif user_input == 4:
    print(my_dict["hobbies"].split(", ")[-1])
elif user_input == 5:
    my_dict["hobbies"]+= ", Cooking"
elif user_input == 6:
    d = my_dict["birth_date"]
    t = (d[:2],d[3:5],d[6:])
    print(t)
elif user_input == 7:
    da = my_dict["birth_date"]
    birthDate = datetime.strptime(da,'%d.%m.%Y')
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    my_dict["age"] = age
    print(age)

