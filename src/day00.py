import sys

part1 = 0
part2 = 0

f = open(sys.argv[1])
data = f.read().strip().split()
print(data)

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
