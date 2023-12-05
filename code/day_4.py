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

print(part_1())
