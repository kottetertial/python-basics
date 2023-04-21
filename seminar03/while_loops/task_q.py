# Q Sequence sum
previous = -1
sequence_sum = 0
while True:
    element = int(input())
    if element == previous == 0:
        break
    sequence_sum += element
    previous = element

print(sequence_sum)
