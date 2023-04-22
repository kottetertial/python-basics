lst = input().split()

lst_unique = []
for elem in lst:
    if elem not in lst_unique:
        lst_unique.append(elem)

print(len(lst_unique))
