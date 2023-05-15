# S Triangle type
a = int(input())
b = int(input())
c = int(input())

a, b, c = sorted([a, b, c])
if a + b <= c and a + c <= b and b + c <= a:
    print("impossible")
elif c ** 2 == a ** 2 + b ** 2:
    print("rectangular")
elif c ** 2 > a ** 2 + b ** 2:
    print("obtuse")
else:
    print("acute")
