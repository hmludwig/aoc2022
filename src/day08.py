import sys

part1 = 0
part2 = 0

f = open(sys.argv[1])
data = f.read().strip().split()
data = [list(x) for x in data]
data = [list(map(int, x)) for x in data]

height = len(data)
width = len(data[0])

part1 += 2 * height + 2 * width - 4
for i in range(1, height - 1):
    for j in range(1, width - 1):
        pos = data[i][j]

        up = data[:i]
        up = [x[j] for x in up]
        down = data[i + 1:]
        down = [x[j] for x in down]
        right = data[i][j + 1:]
        left = data[i][:j]

        if max(up) < pos or max(down) < pos or max(right) < pos or max(
                left) < pos:
            part1 += 1

        s_up, s_down, s_right, s_left = 0, 0, 0, 0
        for x in reversed(up):
            if x < pos:
                s_up += 1
            else:
                s_up += 1
                break

        for x in down:
            if x < pos:
                s_down += 1
            else:
                s_down += 1
                break

        for x in right:
            if x < pos:
                s_right += 1
            else:
                s_right += 1
                break

        for x in reversed(left):
            if x < pos:
                s_left += 1
            else:
                s_left += 1
                break

        part2 = max(part2, s_up * s_down * s_right * s_left)

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
