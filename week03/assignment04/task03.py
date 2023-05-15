deposit = 100 * int(input())
interest_rate = int(input())
target_deposit = 100 * int(input())

years = 0
while deposit < target_deposit:
    deposit += deposit * interest_rate // 100
    years += 1

print(years)
