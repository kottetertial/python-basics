# E First and last entry
string = input()

f_idx_left = string.find("f")
if f_idx_left != -1:
    f_idx_right = string.rfind("f")
    if f_idx_left == f_idx_right:
        print(f_idx_left)
    else:
        print(f_idx_left, f_idx_right)
