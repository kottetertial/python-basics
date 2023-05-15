# N Chess board
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if x2 - x1 == y2 - y1 or y2 == y1 and x2 - x1 % 2 == 0 or x2 == x1 and y2 - y1 % 2 == 0:
    print("YES")
else:
    print("NO")
