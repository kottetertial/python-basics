ip = input()

dots = 0
number = ""
for c in ip:
    if c not in "1234567890.":
        print("NO")
        break
    if c != ".":
        number += c
        continue
    dots += 1
    if dots > 3:
        print("NO")
        break
    if number and 0 <= int(number) <= 255:
        number = ""
        continue
    print("NO")
    break
else:
    if dots == 3:
        print("YES")
    else:
        print("NO")
