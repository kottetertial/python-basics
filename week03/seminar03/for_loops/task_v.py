# V Wonderful Numbers
a = int(input())
b = int(input())

for i in range(a, b + 1):
    ones = i % 10
    tens = i % 100 // 10
    hundreds = i // 100 % 10
    thousands = i // 1000

    if ones == tens == hundreds != thousands \
            or ones == tens == thousands != hundreds \
            or ones == hundreds == thousands != tens \
            or tens == hundreds == thousands != ones:
        print(i)
