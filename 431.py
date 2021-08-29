

msg = input("Guess a letter:")

if ((len(msg) == 1) and (msg.isalpha())):
    print(msg.lower())


else:
    if ((len(msg) > 1) and (not msg.isalpha())):
        print("E3")
    elif (len(msg) > 1):
        print("E1")
    elif (not msg.isalpha()):
        print("E2")