# L Replacing inside a fragment
string = input()

left_idx = string.find("h")
right_idx = string.rfind("h")
if left_idx == right_idx:
    print(string)
else:
    print(string[:left_idx + 1] + string[left_idx + 1:right_idx].replace("h", "H") + string[right_idx:])
