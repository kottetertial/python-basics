# L Queen move
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if x2 != x1 and y2 == y1 or y2 != y1 and x2 == x1 or x2 - x1 == y2 - y1:
    print("YES")
else:
    print("NO")
