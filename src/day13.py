import sys


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left == right:
            return None
        else:
            return left < right
    elif isinstance(left, list) and isinstance(right, list):
        for i in range(min(len(left), len(right))):
            result = compare(left[i], right[i])
            if result is not None:
                return result
        if len(left) == len(right):
            return None
        else:
            return len(left) < len(right)
    elif isinstance(left, int):
        return compare([left], right)
    elif isinstance(right, int):
        return compare(left, [right])
    else:
        return None


def bubble_sort(items):
    n = len(items)
    for i in range(n):
        sorted = True
        for j in range(n - 1 - i):
            if compare(items[j + 1], items[j]):
                items[j], items[j + 1] = items[j + 1], items[j]
                sorted = False
        if sorted:
            break
    return items


part1 = 0
part2 = 0

f = open(sys.argv[1])
data = f.read().strip().split('\n\n')

packets = [[[2]], [[6]]]
for i, pair in enumerate(data):
    left, right = pair.split('\n')
    left, right = eval(left), eval(right)
    packets.append(left)
    packets.append(right)

    part1 += i + 1 if compare(left, right) == 1 else 0

packets = bubble_sort(packets)
part2 = (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
