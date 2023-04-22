heights = [int(i) for i in input().split()]
ivans_height = int(input())

for i in range(1, len(heights) + 1):
    next_person = heights[i - 1]
    if ivans_height > next_person:
        print(i)
        break
    if i == len(heights):
        print(i + 1)
