s = "word"
for i in s:
    if i == "w":
        print(i, end="")
        continue
    print(i * 2, end="")

print()

for i in s:
    if i == "r":
        break
    print(i * 2, end="")

print()

s = "Kirill loves his worK"
for i in s:
    if i == "K":
        print("K is in the string")
        break
else:
    print("K is not in the string")
