n = int(input())

result = 1
factorial = 1
for i in range(2, n + 1):
    factorial *= i
    result += factorial

print(result)
