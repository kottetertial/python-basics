# X Notebook storage
warehouse_x = int(input())
warehouse_y = int(input())
warehouse_z = int(input())

laptop_x = int(input())
laptop_y = int(input())
laptop_z = int(input())

max_laptops = 0

per_x, per_y, per_z = warehouse_x // laptop_x, warehouse_y // laptop_y, warehouse_z // laptop_z
pos_1 = per_x * per_y * per_z

if pos_1 > max_laptops:
    max_laptops = pos_1

per_x, per_y, per_z = warehouse_x // laptop_x, warehouse_y // laptop_z, warehouse_z // laptop_y
pos_2 = per_x * per_y * per_z

if pos_2 > max_laptops:
    max_laptops = pos_2

per_x, per_y, per_z = warehouse_x // laptop_y, warehouse_y // laptop_x, warehouse_z // laptop_z
pos_3 = per_x * per_y * per_z

if pos_3 > max_laptops:
    max_laptops = pos_3

per_x, per_y, per_z = warehouse_x // laptop_z, warehouse_y // laptop_x, warehouse_z // laptop_y
pos_4 = per_x * per_y * per_z

if pos_4 > max_laptops:
    max_laptops = pos_4

per_x, per_y, per_z = warehouse_x // laptop_y, warehouse_y // laptop_z, warehouse_z // laptop_x
pos_5 = per_x * per_y * per_z

if pos_5 > max_laptops:
    max_laptops = pos_5

per_x, per_y, per_z = warehouse_x // laptop_z, warehouse_y // laptop_y, warehouse_z // laptop_x
pos_6 = per_x * per_y * per_z

if pos_6 > max_laptops:
    max_laptops = pos_6

print(max_laptops)
