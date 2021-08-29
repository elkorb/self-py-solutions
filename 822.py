def sort_prices(list_of_tuples):
    return sorted(list_of_tuples,key=get_price,reverse=True)

def get_price(t):
    return t[1]