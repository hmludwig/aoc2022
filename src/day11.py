import sys

part1 = 0
part2 = 0

f = open(sys.argv[1])
data = f.read().strip().split('\n\n')


def parse_data(data):
    monkeys = []
    for monkey in data:
        monkey = [x.strip() for x in monkey.split('\n')]
        name = monkey[0].split(' ')[1].replace(':', '')
        items = eval('[' + monkey[1].split(': ')[1] + ']')
        operation = eval('lambda old: ' +
                         monkey[2].split(': ')[1].split(' = ')[1])
        test = eval('lambda item, mod: ' + monkey[4].split()[-1] +
                    'if item % mod  == 0 else ' + monkey[5].split()[-1])
        mod = int(monkey[3].split()[-1])
        monkeys.append(Monkey(name, items, operation, test, mod))

    return monkeys


class Monkey():

    def __init__(self, name, items, operation, test, mod):
        self.name = name
        self.items = items
        self.operation = operation
        self.test = test
        self.mod = mod
        self.counter = 0

    def inspect(self, mod=None):
        for item in self.items:
            item = self.operation(item)

            if mod is None:
                item = item // 3
            else:
                item = item % mod

            self.counter += 1
            yield item

        self.items = []

    def add_item(self, item):
        self.items.append(item)


monkeys = parse_data(data)
for n in range(20):
    for monkey in monkeys:
        inspected_items = list(monkey.inspect())
        for item in inspected_items:
            tmp = monkey.test(item, monkey.mod)
            monkeys[tmp].add_item(item)

counts = sorted([monkey.counter for monkey in monkeys])
part1 = counts[-1] * counts[-2]

mod = 1
for monkey in monkeys:
    mod *= monkey.mod

monkeys = parse_data(data)
for n in range(10000):
    for monkey in monkeys:
        inspected_items = list(monkey.inspect(mod))
        for item in inspected_items:
            tmp = monkey.test(item, monkey.mod)
            monkeys[tmp].add_item(item)

counts = sorted([monkey.counter for monkey in monkeys])
part2 = counts[-1] * counts[-2]

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
