import math

scallops_per_pan = int(input())
time_per_scallop = 2 * int(input())
number_of_scallops = int(input())

print(math.ceil(number_of_scallops / scallops_per_pan) * time_per_scallop)
