# E Neighbours of the same sign
lst = input().split()

for i in range(1, len(lst)):
    current = int(lst[i])
    previous = int(lst[i - 1])
    if current * previous > 0:
        print(previous, current)
        break
