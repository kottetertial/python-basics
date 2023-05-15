lst_1 = [1, 2, 3, 4, 5, 6]
print(lst_1)

lst_2 = list((1, 2, 3, 4, 5, 6))
print(lst_2)

lst_3 = [i for i in range(1, 7)]
print(lst_3)

lst_4 = list(range(1, 7))
print(lst_4)

print(lst_1 == lst_2 == lst_3 == lst_4)

lst_5 = "Kirill, Anna, Rita, John".split(", ")
print(list(lst_5))

random_list = [1, 2, 3, 4, 5, 6]
random_list[0] = 7
random_list[-1] += 7
print(random_list)
