queens = []
for i in range(8):
    queen = [int(coordinate) for coordinate in input().split()]
    queens.append(queen)
    for another_queen in queens[:i]:
        if (queen[0] == another_queen[0]) ^ (queen[1] == another_queen[1]) \
                or (queen[0] - another_queen[0]) ** 2 == (queen[1] - another_queen[1]) ** 2:
            print("YES")
            break
    else:
        continue
    break
else:
    print("NO")
