import math
from decimal import Decimal

print(round(7.884))
print(round(7.884, 2))

print(round(3.49))

very_small_number = (0.35 ** 0.0099995798) / (10 ** 9)
print(very_small_number)
print(round(very_small_number))

print(round(1.50))
print(round(2.50))
print(round(2.505, 2))

print(Decimal(2.505))

print(math.ceil(7.00009))
print(math.floor(7.00009))
