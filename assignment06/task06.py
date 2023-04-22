lst = input().split()

for i in range(len(lst)):
    elem = lst[i]
    if elem not in lst[:i] and elem not in lst[i + 1:]:
        print(elem, end=" ")
