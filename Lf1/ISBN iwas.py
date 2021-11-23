x = int(input("Number"))
a = x % 10
print(a)
x = x//10
b = x % 10
print(b)
x = x//10
c = x % 10
print(c)
x = x//10
d = x % 10
print(d)
x = x//10
e = x % 10
print(e)
x = x//10
f = x % 10
print(f)
x = x//10
g = x % 10
print(g)
x = x//10
h = x % 10
print(h)
x = x//10
i = x % 10
print(i)
print((a*9+b*8+c*7+d*6+e*5+f*4+g*3+h*2+i*1) % 11)
