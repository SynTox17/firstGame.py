zahl1 = int(input("Deine Zahl"))
zahl2 = int(input("deine Zahl"))
rechenzeichen = input("Dein Operator")

if rechenzeichen == "+":
    print(zahl1 + zahl2)
elif rechenzeichen == "-":
    print(zahl1 - zahl2)
elif rechenzeichen == "*":
    print(zahl1 * zahl2)
elif rechenzeichen == "/":
    if not(zahl1, zahl2 == 0):
        print(zahl1 / zahl2)
    else:
        print("nicht durch null")