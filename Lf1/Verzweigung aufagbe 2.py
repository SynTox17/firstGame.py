hund = int(input("das alter"))
if hund == 1:
    print("Er ist 12")
elif hund  == 2:
    print("Er ist 22")
elif hund > 2:
    hund = hund - 2
    hund = hund * 5 + 22
    print(hund)
# Manschaft
erg1 = int(input("Heim"))
erg2 = int(input("Auswerts"))
tip1 = int(input("Heim"))
tip2 = int(input("Auswerts"))
print(erg1, ":",  erg2,)
if erg1 == tip1 and erg2 == tip2:#Ein Fehler versuche es mehr aufzuteilen
        print("3 Punkte\n")
if erg1 or erg2 == tip1 or tip2:
    print("Ein Punkt")
if erg1 or erg2 != tip1 or tip2:
    print("0 Punkte")
#uhrzeit umrechnen
hn = 13
mn = 18
sn = 10
h = int(input("Stunde"))
m = int(input("Minute"))
s = int(input("Sekunde"))
print(h, m, s)
hn = hn + h
mn = mn + m
sn = sn + s
print(hn, mn, sn)
