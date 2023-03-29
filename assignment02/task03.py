a = float(input())
b = float(input())
c = float(input())

semi_perimeter = (a + b + c) / 2
area = (semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c)) ** 0.5
print(round(area, 5))
