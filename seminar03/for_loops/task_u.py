# U Wonderful Numbers
a = int(input())
b = int(input())

for i in range(a, b + 1):
    if i // 1000 == i % 10 and i // 100 % 10 == i % 100 // 10:
        print(i)
