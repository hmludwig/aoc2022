import sys

part1 = ''
part2 = ''

f = open(sys.argv[1])
drawing, moves = f.read().split('\n\n')
print(drawing, end='\n\n')

#'[x]_[x]_[x]'
drawing = [x.replace('[', ' ').replace(']', ' ') for x in drawing.split('\n')]
stacks1 = [[] for _ in range(int(drawing[-1][-2]))]
stacks2 = [[] for _ in range(int(drawing[-1][-2]))]

for k, row in enumerate(reversed(drawing)):
    if k == 0: continue

    for n, i in enumerate(range(1, len(row), 4)):
        if row[i] != ' ':
            stacks1[n].append(row[i])
            stacks2[n].append(row[i])

moves = moves.splitlines()
for move in moves:
    move = move.split()
    amount = int(move[1])

    t_list = []
    for _ in range(amount):
        tmp1 = stacks1[int(move[3]) - 1].pop()
        tmp2 = stacks2[int(move[3]) - 1].pop()

        stacks1[int(move[-1]) - 1].append(tmp1)
        t_list.append(tmp2)
    stacks2[int(move[-1]) - 1] += list(reversed(t_list))

for stack in stacks1:
    part1 += stack.pop()

for stack in stacks2:
    part2 += stack.pop()

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
