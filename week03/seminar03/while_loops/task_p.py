# P Number of elements equal to the maximum
n = 0
current_max = 0
while True:
    current_element = int(input())
    if current_element == 0:
        break
    if current_element == current_max:
        n += 1
    elif current_element > current_max:
        current_max, n = current_element, 1

print(n)
