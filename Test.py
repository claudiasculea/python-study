from math import sqrt
from tabulate import tabulate
def read_int(variable):
    print(f"Insert {variable} = ")

    return int(input())

x = read_int("x")
g = read_int("g")

while g!= round(sqrt(x), 4):

    x_div_g = x/g
    g = round((g + x_div_g) / 2, 4)
    print(g)


