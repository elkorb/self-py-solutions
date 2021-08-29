msg = input("Enter a word:")

if msg.replace(" " ,"").lower() == msg[::-1].replace(" " ,"").lower():
    print("OK")
else:
    print("NOT")