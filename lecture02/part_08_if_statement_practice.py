num = int(input())
if num > 0:
    print("The number is positive.")

eligibility = False
age = int(input("How old are you? "))
if age >= 18:
    eligibility = True
    print("Eligible! You can proceed!")
