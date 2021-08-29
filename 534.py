def last_early(my_str):
    s = my_str.lower()
    if (s.find(s[-1],0,-1) != -1):
        return True
    else:
        return False



print(last_early("happy birthday"))

print(last_early("best of luck"))

print(last_early("Wow"))

print(last_early("X"))