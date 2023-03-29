rate = int(input())

dollars = int(input())
cents = dollars * 100 + int(input())

years = int(input())

for _ in range(years):
    cents += cents * rate // 100

print(cents // 100, cents % 100)
