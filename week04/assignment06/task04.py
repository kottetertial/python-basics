lst = input().split()
k, c = input().split()

lst.insert(int(k), c)
for elem in lst:
    print(elem, end=" ")
