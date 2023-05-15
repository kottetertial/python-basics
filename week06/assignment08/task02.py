def is_prime(n):
    if n <= 1:
        print("NO")
        return
    for i in range(2, n):
        if n % i == 0:
            print("NO")
            break
    else:
        print("YES")


a = int(input())
is_prime(a)
