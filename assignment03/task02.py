x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

moved_rows = x2 - x1
moved_columns = y2 - y1
if moved_rows != 0 and moved_columns != 0 and moved_rows % moved_columns == 0:
    print("YES")
else:
    print("NO")
