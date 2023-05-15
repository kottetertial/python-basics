n = int(input())

idx = 0
result = -1
fibonacci = [0, 1]
while True:
    if fibonacci[idx] == n:
        result = idx
        break
    idx += 1
    if idx < 2:
        continue
    fibonacci.append(fibonacci[idx - 1] + fibonacci[idx - 2])
    if fibonacci[idx - 1] < n < fibonacci[idx]:
        break

print(result)
