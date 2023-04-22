# F Greater than both neighbours
lst = input().split()

counter = 0
for i in range(1, len(lst) - 1):
    current = int(lst[i])
    previous = int(lst[i - 1])
    next_item = int(lst[i + 1])
    if previous < current and next_item < current:
        counter += 1
print(counter)
