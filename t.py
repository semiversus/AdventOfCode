items = [[54, 61, 97, 63, 74], [61, 70, 97, 64, 99, 83, 52, 87], [60, 67, 80, 65], [61, 70, 76, 69, 82, 56], [79, 98], [72, 79, 55], [63], [72, 51, 93, 63, 80, 86, 81]]
operations = [lambda v:v * 7, lambda v:v + 8, lambda v:v * 13, lambda v:v + 7, lambda v:v + 2, lambda v:v + 1, lambda v:v + 4, lambda v:v * v]
test = [lambda v:v % 17 == 0, lambda v:v % 2 == 0, lambda v:v % 5 == 0, lambda v:v % 3 == 0, lambda v:v % 7 == 0, lambda v:v % 13 == 0, lambda v:v % 19 == 0, lambda v:v % 11 == 0]
passing_monkey = [(3, 5), (6, 7), (6, 1), (2, 5), (3, 0), (1, 2), (4, 7), (4, 0)]

inspections = [0] * len(items)

for round in range(10000):
    if round % 100 == 0:
        print(round)
    for monkey_index in range(len(items)):
        for item in items[monkey_index]:
            worry_level = (operations[monkey_index](item)) % (2 * 3 * 5 * 7 * 11 * 13 * 17 * 19)
            items[passing_monkey[monkey_index][test[monkey_index](worry_level)]].append(worry_level)
            inspections[monkey_index] += 1
        items[monkey_index].clear()

from operator import mul
mul(*tuple(sorted(inspections))[-2:])