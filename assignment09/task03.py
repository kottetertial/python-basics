def recursive_sum(a, b):
    if b == 0:
        return a
    return 1 + recursive_sum(a, b - 1)


a = int(input())
b = int(input())
print(recursive_sum(a, b))
