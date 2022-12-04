import sys

f = open(sys.argv[1])
data = f.read().strip().split()

part1 = 0
part2 = 0

for d in data:
    a, b = d.split(',')
    a1, a2 = list(map(int, a.split('-')))
    b1, b2 = list(map(int, b.split('-')))
    
    if a1 <= b1 and a2 >= b2 or b1 <= a1 and  b2 >= a2:
        part1 += 1

    if max(a1, b1) <= min(a2, b2):
        part2 += 1

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
