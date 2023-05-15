# Y Triangular sequence
n = int(input())

current_term = 0
term_start_idx = 0
for i in range(n):
    if i - term_start_idx == current_term:
        current_term += 1
        term_start_idx = i
    print(current_term, end=" ")
