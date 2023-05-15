n = int(input("Your number: "))
is_even = n % 2 == 0
print("Is even?", is_even)

x = int(input("First number: "))
y = int(input("Second number: "))
print(x == y)
print(x != y)
print(x > y)
print(x > y)
print(x >= y)
print(x <= y)

password = input("Your password: ")
is_correct = password == "Qwerty"
print("Is the password correct?", is_correct)
print(password < "Qwerty")

# Return the Unicode code point for a one-character string.
print(ord("Q"))
print(ord("q"))
