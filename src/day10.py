import sys

part1 = 0
part2 = ''

f = open(sys.argv[1])
data = f.read().strip().split('\n')


def check_cycle(cycle, x, crt):
    global part1
    global part2
    if cycle in [20, 60, 100, 140, 180, 220]:
        part1 += cycle * x
    elif cycle in [40, 80, 120, 160, 200, 240]:
        part2 += crt + '\n'
        return ''
    return crt


def draw(crt, cycle, sprite_pos):
    if sprite_pos[cycle % 40] == '#':
        crt += '#'
    else:
        crt += '.'
    return crt


x = 1
crt = ''
cycle = 0
sprite_pos = '###' + '.' * 37

for line in data:
    line = line.split()
    if line[0] == 'noop':
        crt = draw(crt, cycle, sprite_pos)
        cycle += 1
        crt = check_cycle(cycle, x, crt)
    elif line[0] == 'addx':
        for _ in range(2):
            crt = draw(crt, cycle, sprite_pos)
            cycle += 1
            crt = check_cycle(cycle, x, crt)
        x += int(line[1])
        sprite_pos = '.' * (x - 1)
        sprite_pos += '###'
        sprite_pos += '.' * (40 - len(sprite_pos))

print(f'Part 1: {part1}')
print(f'Part 2:\n{part2}')
