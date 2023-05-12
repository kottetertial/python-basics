# F Second entry
string = input()

first_idx = string.find("f")
if first_idx == -1:
    print(-2)
else:
    second_idx = string.find("f", first_idx + 1)
    print(second_idx)
