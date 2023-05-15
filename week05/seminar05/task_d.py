# D Rearrange two words
string = input()
words = string.split()
print(*words[::-1])
print(words[1], words[0])

space_idx = string.find(" ")
print(string[space_idx + 1:], string[:space_idx])
