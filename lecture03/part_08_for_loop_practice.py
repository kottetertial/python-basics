for el in range(1, 11):
    print(el)

for el in "randomstring":
    print(el, end=" ")

print()
for el in [1, 3, 6, 8, 9, 100]:
    print(el)

user_set = ["toothpaste", "apple", "banana"]
for el in user_set:
    if el == "apple":
        print("You get a discount!")
    else:
        print("Great choice!")

user_set = [100, 1000, 10, 1000, 1000000, 9999]
for el in user_set:
    print("You paid VAT", 0.2 * el)
