# M Number of elements that are greater than the previous element in the sequence
n = 0
previous = 0
while True:
    current = int(input())
    if current == 0:
        break
    if previous and current > previous:
        n += 1
    previous = current

print(n)
