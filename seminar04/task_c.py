# C Positive elements
lst = input().split()

counter = 0
for x in lst:
    if int(x) > 0:
        counter += 1
print(counter)
