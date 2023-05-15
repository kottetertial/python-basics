# R Insert element
lst = input().split()
k, c = input().split()

lst.insert(int(k), c)
print(*lst)
