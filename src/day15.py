import sys


def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def check(x, y, sensors, beacons):
    for sx, sy, r in sensors:
        if manhattan_distance((x, y), (sx, sy)) <= r and (x, y) not in beacons:
            return False
    return True


part1 = set()
part2 = 0

f = open(sys.argv[1])
data = f.read().strip().split('\n')

y = 2_000_000

sensors = set()
beacons = set()
bs = set()
for d in data:
    d = d.replace(',', '')
    sensor, beacon = d.split(': ')

    sensor = sensor.split()
    sx = int(sensor[-2].split('=')[-1])
    sy = int(sensor[-1].split('=')[-1])
    if sy == y:
        part1.add(sx)

    beacon = beacon.split()
    bx = int(beacon[-2].split('=')[-1])
    by = int(beacon[-1].split('=')[-1])
    if by == y:
        bs.add(bx)

    r = manhattan_distance((sx, sy), (bx, by))

    sensors.add((sx, sy, r))
    beacons.add((bx, by))

    if y in list(range(sy - r, sy + r)):
        min_x, max_x = sx - r, sx + r
        y_delta = abs(sy - y)
        min_x += y_delta
        max_x -= y_delta

        part1.update(list(range(min_x, max_x + 1)))

part1 -= bs

for sx, sy, r in sensors:
    for dx in range(r + 2):
        dy = (r + 1) - dx
        for mx, my in [(-1, 1), (1, -1), (-1, -1), (1, 1)]:
            x, y = sx + (dx * mx), sy + (dy * my)
            if not (0 <= x <= 4_000_000 and 0 <= y <= 4_000_000):
                continue
            if check(x, y, sensors, beacons):
                part2 = x * 4_000_000 + y
                break
        if part2 != 0:
            break
    if part2 != 0:
        break

print(f'Part 1: {len(part1)}')
print(f'Part 2: {part2}')
