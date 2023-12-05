def part_1():
    sum = 0
    file = open('../input/day_4.txt')
    for line in file:
        cost = 0
        lists = line.split(':')[1].split('|')
        winners = [int(n.strip()) for n in lists[0].split(' ') if n != '']
        nums = [int(n.strip()) for n in lists[1].split(' ') if n != '']
        for i in nums:
            if i in winners:
                cost = cost * 2 if cost > 0 else 1
        sum = sum + cost
    return sum


def part_2():
    lines = open('../input/day_4.txt').read().split('\n')
    cards = [1 for n in range(len(lines))]
    for k in range(len(lines)):
        count = 0
        lists = lines[k].split(':')[1].split('|')
        winners = [int(n.strip()) for n in lists[0].split(' ') if n != '']
        nums = [int(n.strip()) for n in lists[1].split(' ') if n != '']
        for i in nums:
            if i in winners:
                count = count + 1
        for i in range(1, count + 1):
            try:
                cards[k + i] = cards[k + i] + cards[k]
            except:
                pass
    return sum(cards)


print(part_1())
print(part_2())
