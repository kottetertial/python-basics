num = int(input())
if num > 0:
    print("The number is positive.")
elif num == 0:
    print("The number is zero.")
else:
    print("The number is negative.")

# Light User 1-2 visits
# Medium User 3-10 visits
# Heavy User 11+ visits
num_visits = int(input("Number of visits: "))
if num_visits > 10:
    print("Heavy User!")
elif 3 <= num_visits <= 10:
    print("Medium User!")
else:
    print("Light User!")

# Nested Conditions
if num_visits > 2:
    if num_visits > 10:
        print("Heavy User!")
    else:
        print("Medium User!")
else:
    print("Light User!")
