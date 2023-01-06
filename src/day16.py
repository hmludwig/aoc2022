import sys


def solve(pos, time, flow, answer, mask):
    answer[mask] = max(answer.get(mask, 0), flow)
    for node in Flow:
        new_time = time - Time[pos][node] - 1
        if Mask[node] & mask or new_time <= 0:
            continue
        solve(node, new_time, flow + new_time * Flow[node], answer,
              mask | Mask[node])
    return answer


part1 = 0
part2 = 0

f = open(sys.argv[1])
data = f.read().strip().split('\n')

Graph = {}
Flow = {}
for line in data:
    line = line.replace('=', ' ').replace(',', '').replace(';', '').split()
    Graph[line[1]] = set(line[10:])
    flow = int(line[5])
    if flow != 0:
        Flow[line[1]] = flow

Mask = {x: 1 << i for i, x in enumerate(Flow)}

# Floyd-Warshall
Time = {
    x:
    {y: 1 if y in Graph[x] else 0 if y == x else float('+inf')
     for y in Graph}
    for x in Graph
}
for k in Time:
    for i in Time:
        for j in Time:
            Time[i][j] = min(Time[i][j], Time[i][k] + Time[k][j])

part1 = max(solve('AA', 30, 0, {}, 0).values())
solution = solve('AA', 26, 0, {}, 0)
part2 = max(f1 + f2 for m1, f1 in solution.items()
            for m2, f2 in solution.items() if not m1 & m2)

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
