import sys


def min_max(nums):
    return min(nums), max(nums)


def print_cave(cave):
    minx, maxx = min_max([x for x, _ in cave])
    miny, maxy = min_max([y for _, y in cave])
    for y in range(miny - 1, maxy + 2):
        for x in range(minx - 1, maxx + 2):
            print(cave.get((x, y), '.'), end='')
        print()


def create_cave(data):
    cave = dict()
    for row in data:
        row = row.split(' -> ')
        n = len(row)
        for i in range(n - 1):
            a1, b1 = map(int, row[i].split(','))
            a2, b2 = map(int, row[i + 1].split(','))
            da, db = abs(a2 - a1), abs(b2 - b1)
            if da == 0:
                for k in range(db + 1):
                    if b1 < b2:
                        cave[a1, b1 + k] = '#'
                    else:
                        cave[a2, b2 + k] = '#'
            elif db == 0:
                for k in range(da + 1):
                    if a1 < a2:
                        cave[a1 + k, b1] = '#'
                    else:
                        cave[a2 + k, b2] = '#'

    return cave


def fall(cave):
    global sandx
    global sandy
    global part1

    while (sandx, sandy + 1) not in cave:
        sandy += 1
        if sandy > maxy and part1 == 0:
            part1 = sum(x == 'o' for x in cave.values())


part1 = 0
part2 = 0

f = open(sys.argv[1])
data = f.read().strip().split('\n')

cave = create_cave(data)
print_cave(cave)

_, maxy = min_max([y for _, y in cave])
minx, maxx = min_max([x for x, _ in cave])
delta = 200
for x in range(minx - delta, maxx + delta):
    cave[x, maxy + 2] = '#'

done = False
while True:
    sandx, sandy = 500, 0
    while True:
        done = fall(cave)
        if done:
            break

        if (sandx - 1, sandy + 1) not in cave:
            sandx -= 1
            sandy += 1
        elif (sandx + 1, sandy + 1) not in cave:
            sandx += 1
            sandy += 1
        else:
            break
    if done:
        break
    cave[sandx, sandy] = 'o'
    if sandx == 500 and sandy == 0:
        break

part2 = sum(x == 'o' for x in cave.values())

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
