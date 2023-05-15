# J Row
heights = [int(i) for i in input().split()]
petyas_height = int(input())

for i in range(1, len(heights) + 1):
    next_person = heights[i - 1]
    if petyas_height > next_person:
        print(i)
        break
    if i == len(heights):
        print(i + 1)
