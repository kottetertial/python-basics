# F Morning running
x = float(input())
y = float(input())

days = 1
while x < y:
    days += 1
    x += x / 10

print(days)
