# P Switch min and max elements
lst = [int(i) for i in input().split()]

min_idx = 0
max_idx = 0
min_elem = None
max_elem = None
for i in range(len(lst)):
    elem = lst[i]
    if not min_elem or elem < min_elem:
        min_elem, min_idx = elem, i
    if not max_elem or elem > max_elem:
        max_elem, max_idx = elem, i

lst[min_idx], lst[max_idx] = max_elem, min_elem
print(*lst)
