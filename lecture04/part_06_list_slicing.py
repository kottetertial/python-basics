lst_1 = [1, 2, 3, 4, 5, 6, 7]
print(lst_1[0])
print(lst_1[2:])
print(lst_1[2:6])
print(lst_1[2:6:2])
print(lst_1[5::-1])

lst_1.append(8)
print(lst_1)

lst_1.append([9, 10])
print(lst_1)

lst_1.extend([11, 12])
print(lst_1)

lst_1.insert(1, 13)
print(lst_1)

lst_2 = [14, 15, 16, 17]
lst_3 = lst_1 + lst_2
print(lst_3)

lst_4 = lst_3 * 2
print(lst_4)

lst_1.pop()
print(lst_1)

del lst_1[3]
print(lst_1)

del lst_1[:3]
print(lst_1)

lst_1.pop(2)
print(lst_1)
