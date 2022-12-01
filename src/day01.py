import sys

f = open(sys.argv[1])
data = f.read().strip().split('\n\n')


cals = []

for d in data:
    elf = d.split('\n')
    tmp = 0
    for cal in elf:
        tmp += int(cal)
    cals.append(tmp)

cals = sorted(cals)

print(f'Part 1: {cals[-1]}')
print(f'Part 2: {cals[-1] + cals[-2] + cals[-3]}')

