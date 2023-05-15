lst = input().split()

max_elem = None
max_elem_idx = 0
for i in range(len(lst)):
    elem = int(lst[i])
    if not max_elem or elem > max_elem:
        max_elem, max_elem_idx = elem, i

print(max_elem, max_elem_idx)
