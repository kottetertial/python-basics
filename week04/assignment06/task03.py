lst = input().split()
k = int(input())

lst.pop(k)
for elem in lst:
    print(elem, end=" ")
