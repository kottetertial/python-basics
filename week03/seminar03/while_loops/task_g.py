# G Bank interest
starting_deposit = int(input()) * 100
interest_rate = int(input())
target_deposit = int(input()) * 100

years = 0
while starting_deposit < target_deposit:
    years += 1
    starting_deposit += starting_deposit * interest_rate // 100

print(years)
