# H Fragment reversal
string = input()

left_idx = string.find("h")
right_idx = string.rfind("h")
print(string[:left_idx] + string[right_idx:left_idx:-1] + string[right_idx:])
