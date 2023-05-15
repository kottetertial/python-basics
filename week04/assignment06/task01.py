lst = input().split()

for i in range(len(lst)):
    if i % 2 == 0:
        print(lst[i], end=" ")
