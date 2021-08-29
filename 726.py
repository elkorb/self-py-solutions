
def print_all_products(my_list):
    print(my_list)

def print_products_amount(my_list):
    print(len(my_list))
    
def print_is_in_list(prod, my_list):
    print( prod in my_list)

def print_product_amount_in_list(prod,my_list):
   print(my_list.count(prod))

def remove_from_list(prod, my_list):
    my_list.remove(prod)

def add_to_list(prod, my_list):
    my_list.append(prod)

def print_all_illegal_products(my_list):
    for item in my_list:
        if (len(item) < 3 or not item.isalpha()):
            print(item)

def remove_duplicates(my_list):
    final_list = []
    for item in my_list:
        if not item in final_list:
            final_list.append(item) 
    return final_list


products_list = input("please enter the products: ").split(',')    
user_input = 0
while user_input != 9:
    user_input = int(input("""
        Please select your option:
        1. Print the products list.
        2. Print number of products in list.
        3. Print is product in list.
        4. Print how many times the product in list
        5. delete product from list
        6. Add product to list
        7. Print all illegal products
        8. Remove all duplications
        9. Exit
        """))
    if user_input == 1: 
        print_all_products(products_list)
        continue
    elif user_input == 2: 
        print_products_amount(products_list)
        continue
    elif user_input == 3:
        req_prod = input("which product?")
        print_is_in_list(req_prod,products_list)
        continue
    elif user_input == 4:
        req_prod = input("which product?")
        print_product_amount_in_list(req_prod,products_list)
        continue
    elif user_input == 5:
        req_prod = input("which product?")
        remove_from_list(req_prod,products_list)
        continue
    elif user_input == 6:
        req_prod = input("which product?")
        add_to_list(req_prod,products_list)
        continue
    elif user_input == 7:
        print_all_illegal_products(products_list)
        continue
    elif user_input == 8:
        products_list = remove_duplicates(products_list)
        continue
    elif user_input == 9:
        print("Bye Bye")
        break
