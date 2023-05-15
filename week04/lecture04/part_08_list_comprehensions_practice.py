random_list_0 = [i for i in range(1, 10)]
print(random_list_0)

random_list_1 = []
for i in range(0, 101):
    if i % 10 == 0:
        random_list_1.append(i)
print(random_list_1)

random_list_2 = [i for i in range(0, 101) if i % 10 == 0]
print(random_list_2)

print(random_list_1 == random_list_2)
