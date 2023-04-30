fib_cache = [0, 1, 1]


def fib(n):
    if n == len(fib_cache):
        fib_cache.append(fib_cache[n - 1] + fib_cache[n - 2])
    if n < len(fib_cache):
        return fib_cache[n]
    return fib(n - 1) + fib(n - 2)


a = int(input())
print(fib(a))
