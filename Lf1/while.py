m = 1
while m != 6:
   m + 1
   print(m)
   m = m +1
# Aufgabe 2
print("Aufgabe 2 ")

a = 2
while a != 8:
    print(a)
    a = a + 1
# Aufgabe 3
print("Aufgabe 3 ")
v = 1
while v < 21:
    print(v)
    v = v + 2
#Aufgabe 4
print("Aufgabe4")
c = 10
while c > -12:
    print(c)
    c = c - 2
#Aufgabe 5

print("Aufgabe5")
x = 1
y = 0
while x <= 10:
    while y <= 10:
        print(x * y, end=" ")
        y = y + 1
    x = x + 1
    y = 0
    print()


#Aufgabe 6
while str(input("")):
    zahl = int(input("Deine Zahl"))
    zahl = zahl % 7
    if zahl == 0:
        print("Ist teilbar")
    else:
        print("ist nicht teilbar")



