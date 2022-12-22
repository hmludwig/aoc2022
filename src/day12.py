import sys
import heapq

part1 = 0
part2 = 0

f = open(sys.argv[1])
data = [list(row) for row in f.read().strip().split()]


def get_height(grid, row, column):
    pos = grid[row][column]
    if pos == "S":
        return 0
    elif pos == "E":
        return 25
    else:
        return ord(pos) - ord("a")


def get_neighbors(grid, row, column):
    height = get_height(grid, row, column)
    neighbors = []
    for d_row, d_column in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        r_t, c_t = row + d_row, column + d_column
        if 0 <= r_t < len(grid) and 0 <= c_t < len(grid[0]):
            if get_height(grid, r_t, c_t) <= height + 1:
                neighbors.append((r_t, c_t))
    return neighbors


def steps_dijkstra(grid, start, end):
    visited = set()
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))

    while priority_queue:
        steps, node = heapq.heappop(priority_queue)

        if node in visited:
            continue
        elif node == end:
            return steps
        else:
            visited.add(node)
            for r_new, c_new in get_neighbors(grid, node[0], node[1]):
                heapq.heappush(priority_queue, (steps + 1, (r_new, c_new)))

    return -1


def get_start_end_pos(grid):
    starts = []
    end = None
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if grid[row][column] == "S":
                start = (row, column)
                starts.append((row, column))
            elif grid[row][column] == "E":
                end = (row, column)
            elif grid[row][column] == "a":
                starts.append((row, column))
    return (start, end, starts)


start, end, starts = get_start_end_pos(data)
part1 = steps_dijkstra(data, start, end)

stepss = []
for start in starts:
    steps = steps_dijkstra(data, start, end)
    if steps != -1:
        stepss.append(steps)
part2 = min(stepss)

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
