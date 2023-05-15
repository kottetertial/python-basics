# I Fragment duplication
string = input()

left_idx = string.find("h")
right_idx = string.rfind("h")
print(string[:right_idx] + string[left_idx + 1:right_idx] + string[right_idx:])
