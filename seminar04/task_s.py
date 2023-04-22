# S Count matching pairs
lst = [int(i) for i in input().split()]

counter = 0
for i in range(len(lst)):
    elem_i = lst[i]
    for j in range(i + 1, len(lst)):
        elem_j = lst[j]
        if elem_i == elem_j:
            counter += 1

print(counter)
