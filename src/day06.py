import sys

part1 = 0
part2 = 0

f = open(sys.argv[1])
data = f.read().strip().split()[0]

for i in range(0, len(data)-3):
    tmp = set(list(data[i:i+4]))
    if len(tmp) == 4:
        part1 = i+4
        break

for i in range(0, len(data)-13):
    tmp = set(list(data[i:i+14]))
    if len(tmp) == 14:
        part2 = i+14
        break

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
