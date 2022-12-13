import sys

part1 = 0
part2 = 0

f = open(sys.argv[1])
data = f.read().strip().split('\n')


def move(x, y, direction):
    if direction == 'R':
        x += 1
    elif direction == 'L':
        x -= 1
    elif direction == 'U':
        y += 1
    elif direction == 'D':
        y -= 1
    return x, y


def move_toward(x, y, target_x, target_y):
    dx, dy = target_x - x, target_y - y
    adx, ady = abs(dx), abs(dy)

    if adx == 2:
        if dx > 0:
            x += 1
        else:
            x -= 1
        if ady == 1:
            y += dy
    if ady == 2:
        if dy > 0:
            y += 1
        else:
            y -= 1
        if adx == 1:
            x += dx

    return x, y


tail_visited1 = set()
tail_visited2 = set()
rope = [(0, 0) for _ in range(10)]

for motion in data:
    direction, amount = motion.split()
    for _ in range(int(amount)):
        rope[0] = move(*rope[0], direction)
        for i in range(1, len(rope)):
            rope[i] = move_toward(*rope[i], *rope[i - 1])
        tail_visited1.add(rope[1])
        tail_visited2.add(rope[-1])

part1 = len(tail_visited1)
part2 = len(tail_visited2)

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
