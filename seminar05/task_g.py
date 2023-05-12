# G Delete a fragment
string = input()

left_idx = string.find("h")
right_idx = string.rfind("h")
print(string[:left_idx] + string[right_idx + 1:])
