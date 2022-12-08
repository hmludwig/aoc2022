import sys
from collections import defaultdict

part1 = 0
part2 = 0

f = open(sys.argv[1])
data = [x.strip() for x in f.readlines()]

path = ''
file_system = defaultdict(list)
for line in data:
    line = line.split()
    if line[0] == '$' and line[1] == 'cd':
        if line[2] == '..':
            path = path.split('/')
            path = '/'.join(path[:-1])
            if path == '':
                path = '.'
        elif line[2] == '/':
            path = '.'
        elif path == '/':
            path += line[2]
        else:
            path += '/' + line[2]
    elif line[0] == '$':
        continue
    elif line[0] == 'dir':
        file_system[path] += defaultdict(list)
    else:
        file_system[path].append(int(line[0]))

folders = defaultdict(lambda: 0)
for key in file_system.keys():
    folders[key] += sum(file_system[key])

for key in reversed(sorted(file_system.keys(), key=lambda key: len(key))):
    if key == '.':
        continue
    tmp = key.split('/')
    tmp = '/'.join(tmp[:-1])
    folders[tmp] += folders[key]

for value in folders.values():
    if value <= 100000:
        part1 += value

space = 70000000
free_space = space - folders['.']
space_needed = 30000000
for value in sorted(folders.values()):
    if value >= space_needed - free_space:
        part2 = value
        break

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
