import sys

f = open(sys.argv[1])
data = [line.strip() for line in f.readlines()]

part1 = 0
part2 = 0

A, X = 1, 1  #Rock
B, Y = 2, 2  #Paper
C, Z = 3, 3  #Scissor

for x in data:
    a, b = x.split(' ')
    a, b = eval(a), eval(b)

    if b == a:
        part1 += 3 + b
    elif b == 3 and a == 1:
        part1 += 0 + b
    elif b == 1 and a == 3:
        part1 += 6 + b
    elif b > a:
        part1 += 6 + b
    elif b < a:
        part1 += 0 + b

    if b == 2:
        part2 += 3 + a
    elif b == 1:
        tmp = a - 1 if a - 1 > 0 else 3
        part2 += tmp
    elif b == 3:
        tmp = a + 1 if a + 1 < 4 else 1
        part2 += 6 + tmp

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
