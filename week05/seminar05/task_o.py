# O Unpacking a string
packed_string = input()

result = ""
quantity = 1
string_quantity = ""
for char in packed_string:
    if char.isdigit():
        string_quantity += char
        continue
    quantity = int(string_quantity) if string_quantity else 1
    result += char * quantity
    quantity, string_quantity = 1, ""

start = 0
while start < len(result):
    print(result[start:start + 40])
    start += 40
