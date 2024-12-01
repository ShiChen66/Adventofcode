from collections import Counter

with open('input.txt') as f:
    values = [line.rstrip() for line in f]

set_1 = []
set_2 = []
for value in values:
    val = value.split()
    set_1.append(int(val[0]))
    set_2.append(int(val[1]))

def part1(set_1, set_2):
    set_1.sort()
    set_2.sort()

    sum = 0

    for x, y in zip(set_1, set_2):
        sum += abs(x-y)

    return sum


def part2(set_1, set_2):
    freq = Counter(set_2)

    sum = 0

    for val in set_1:
        sum += val * freq[val]

    return sum

print(part1(set_1, set_2))
print(part2(set_1, set_2))
