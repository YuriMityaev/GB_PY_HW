from itertools import count, cycle


count_1 = count(10, 2)
cycle_1 = cycle("ABCDE")

for arg in range(7):
    print("(count_1, cycle_1) = ({},{})".format(next(count_1), next(cycle_1)))
