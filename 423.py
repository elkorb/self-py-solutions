temperature = input("Insert the temperature you would like to convert: ")

if temperature[-1].upper() == "F":
    number = float(temperature[:-1])
    print(str(((5 * number) - 160)/9) + "C")
elif temperature[-1].upper() == "C":
    number = float(temperature[:-1])
    print(str(((9 * number) + (32 * 5))/5) + "F")