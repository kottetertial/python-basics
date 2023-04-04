a = int(input())
b = int(input())

# Return the identity of an object
id_a = id(a)
id_b = id(b)
print(id_a)
print(id_b)

print(a is b)
print(id_a == id_b)

print(a is not b)
print(id_a != id_b)
