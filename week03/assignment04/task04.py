n = int(input())

fibonacci = [0, 1]
i = 2
while i <= n:
    fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    i += 1

print(fibonacci[n])
