string = input()

left_part_length = len(string) // 2 + len(string) % 2
left_part = string[:left_part_length]

right_part_length = len(string) - left_part_length + len(string) % 2
right_part = string[right_part_length:]

new_string = right_part + left_part
print(new_string)