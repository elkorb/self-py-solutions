msg = input("Please enter a string:")
half = len(msg)//2
print(msg[:half].lower() + msg[half:].upper())