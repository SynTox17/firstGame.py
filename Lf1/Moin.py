
day = 0
hn = 23
mn = 59
sn = 56
s = int(input("Second"))
sn = sn + s
while sn > 59:
    sn = sn - 60
    mn = mn + 1
    print(sn, "Second")
    print(mn, "Minutes")
while mn > 59:
    mn = mn - 60
    hn = hn + 1
    print(hn, "hour")
while hn == 24:
    hn = hn - 24
    day = day + 1
print("day", day,"hour", hn,"minute", mn,"second", sn, end="")



