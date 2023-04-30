def factorial_loop(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res


def factorial_recursive(n):
    if n == 1:
        return 1
    return n * factorial_recursive(n - 1)


def binomial(n, k):
    return factorial_loop(n) // (factorial_loop(k) * factorial_loop(n - k))


result_1 = factorial_loop(5)
result_2 = factorial_recursive(5)
print(result_1, result_2)

result = binomial(5, 2)
print(result)
