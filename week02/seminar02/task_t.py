# T Subway tickets
n = int(input())

trip_1 = 0
trips_10 = 0
trips_60 = n // 60

n %= 60
if n >= 35:
    trips_60 += 1
else:
    trips_10 = n // 10
    n %= 10
    if n >= 9:
        trips_10 += 1
    else:
        trip_1 = n

print(trip_1, trips_10, trips_60)
