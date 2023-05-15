a = int(input())
b = int(input())
c = int(input())

if a > 0 and b > 0 and c > 0:
    print("The numbers are positive!")
else:
    print("At least one number is not positive!")

if a > 0 or b > 0 or c > 0:
    print("At least one number is positive!")
else:
    print("None of the numbers are positive!")
