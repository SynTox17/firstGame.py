import random

p = 0
a = 0
g = 0
s = 0
u = 0
n = 0

while p < 10:
    print("1=Schere,2=Stein;3=Papier")
    a = int(input("deine Zahl "))
    if (a > 3) or (a < 0):
        print("Unbekannter Fehler nur zahl von 1 bis 3 ")
        quit()
    b = random.randint(1, 3)
    print(b)
    if a == b:
        print("Unentschieden")
        u += 1
        p += 1
    elif (a == 1) and (b == 2):
        print("Verloren er hatte Stein")
        n += 1
        p += 1
        s = 0
    elif (a == 1) and (b == 3):
        print("Gewonnen er hatte Papier")
        p += 1
        s += 1
        g += 1
    elif (a == 2) and (b == 1):
        print("gewonnen! Er hatte Schere")
        p += 1
        s += 1
        g += 1
    elif (a == 2) and (b == 3):
        print("verloren!Er hatte Stein")
        n += 1
        p += 1
        s = 0
    elif (a == 3) and (b == 1):
        print("verloren! Er hatte Schere")
        n += 1
        p += 1
        s = 0
    elif (a == 3) and (b == 2):
        print("Gewonnen! Er hatte stein")
        p += 1
        s += 1
        g += 1
    elif g < 3:
        print("Mies gespielt")
    print(g, s, u, n)
