def hello():
    print("Hello, world!")


def hello_user(user_name):
    print(f"Hello, {user_name}!")


def hello_user_return(user_name):
    return f"Hello, {user_name}!"


def power(a, b):
    return a ** b


def minimum(*nums):
    current_min = nums[0]
    for num in nums[1:]:
        if num < current_min:
            current_min = num
    return current_min


def func(a, b):
    return a * 2, b * 2


hello()
hello_user("Valeriia")

result = hello_user_return("Valeriia")
print(result)

result = power(2, 3)
print(result)

result_1 = minimum(1, 5, 6, 8, 5, 3)
result_2 = minimum(1, 5, 6, 8, 5, 3, 5234, 6, 7, 3, 5, 3, -345, 6)
print(result_1, result_2)

result_1, result_2 = func(3, 6)
print(result_1, result_2)
