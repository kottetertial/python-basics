count = 0
while count < 9:
    print("The count is", count)
    count += 1

flag = True
while flag:
    number = int(input("Guess the number! "))
    if number == 5:
        print("Correct!")
        flag = False

count = 0
while count < 5:
    print(count, "is less than 5")
    count += 1
else:
    print(count, "is not less than 5")
