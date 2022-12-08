import sys

f = open(sys.argv[1])
data = f.read().strip().split()

part1 = 0
part2 = 0

for d in data:
    s1, s2 = slice(0, len(d) // 2), slice(len(d) // 2, len(d))
    l, r = d[s1], d[s2]
    common = list(set(l) & set(r))

    for c in common:
        if c.isupper():
            part1 += ord(c) - ord('A') + 1 + 26
        else:
            part1 += ord(c) - ord('a') + 1

for i in range(0, len(data), 3):
    c = list(set(data[i]) & set(data[i + 1]) & set(data[i + 2]))[0]
    if c.isupper():
        part2 += ord(c) - ord('A') + 1 + 26
    else:
        part2 += ord(c) - ord('a') + 1

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
