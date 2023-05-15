# N Delete every third character
string = input()
for i in range(len(string)):
    if i % 3 == 0:
        continue
    print(string[i], end="")
