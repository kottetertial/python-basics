def calculate(left_term, right_term, operator):
    if operator == "+":
        return left_term + right_term
    if operator == "-":
        return left_term - right_term
    if operator == "*":
        return left_term * right_term
    if operator == "/":
        return left_term / right_term


a = float(input())
b = float(input())
op = input()
print(calculate(a, b, op))
