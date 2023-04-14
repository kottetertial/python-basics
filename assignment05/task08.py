n = int(input())

result = 0
for _ in range(n):
    email = input()
    if "@gmail.com" in email:
        print(email)
