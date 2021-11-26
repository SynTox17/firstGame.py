import time


z = 0
s = 0
m = 0
h = 0
d = 0
if z == 0:
    z += 1
while z > 0:
    s += 1
    time.sleep(1)
    print(d, h, m, s)
    while s > 59:
        s = 0
        m += 1
        time.sleep(1)
        print(d, h, m, s)
        if m > 59:
            m = 0
            h += 1
            print(d, h, m, s)
        if h > 24:
            h = 0
            d += 1
            print(d, h, m, s)
            if d == 10000:
                z = 0
                d = 0
print(d, h, m, s)
