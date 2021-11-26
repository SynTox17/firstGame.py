hund = int(input("das alter"))
if hund == 1:
    print("Er ist 12")
elif hund == 2:
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
day = 0
hn = 23
mn = 59
sn = 59
s = int(input( "Second" ))
sn = sn + s
while sn > 59:
    sn = sn - 60
    mn += 1
    print(sn, "Second")
    print(mn, "Minutes")
while mn > 59:
    mn = mn - 60
    hn += 1
    print(hn, "hour")
while hn >= 24:
    hn = hn - 24
    day += 1
print("day", day,"hour", hn,"minute", mn,"second", sn, end="")

