import re


def part_1():
    sum = 0
    text = open('../input/day_3.txt').read()
    lines = text.split('\n')
    for line_num in range(len(lines)):
        match = re.finditer(r'\d+', lines[line_num])
        for gap in list(match):
            num = ''
            is_valid = False
            for i in range(gap.span()[0], gap.span()[1]):
                num = num + lines[line_num][i]
                if line_num - 1 >= 0:
                    if re.match(r'[^0-9\.]', lines[line_num - 1][i]):  # верх
                        is_valid = True
                if i + 1 < len(lines[line_num]):
                    if re.match(r'[^0-9\.]', lines[line_num][i + 1]):  # право
                        is_valid = True
                if line_num + 1 < len(lines):
                    if re.match(r'[^0-9\.]', lines[line_num + 1][i]):  # низ
                        is_valid = True
                if i - 1 >= 0:
                    if re.match(r'[^0-9\.]', lines[line_num][i - 1]):  # лево
                        is_valid = True
                # диагонали
                if line_num - 1 >= 0 and i - 1 >= 0:
                    if re.match(r'[^0-9\.]', lines[line_num - 1][i - 1]):  # лево-верх
                        is_valid = True
                if line_num - 1 >= 0 and i + 1 < len(lines[line_num]):
                    if re.match(r'[^0-9\.]', lines[line_num - 1][i + 1]):  # право-верх
                        is_valid = True
                if line_num + 1 < len(lines) and i - 1 >= 0:
                    if re.match(r'[^0-9\.]', lines[line_num + 1][i - 1]):  # лево-низ
                        is_valid = True
                if line_num + 1 < len(lines) and i + 1 < len(lines[line_num]):
                    if re.match(r'[^0-9\.]', lines[line_num + 1][i + 1]):  # право-низ
                        is_valid = True
            if is_valid:
                sum = sum + int(num)
    return sum


def part_2():
    sum = 0
    text = open('../input/day_3.txt').read()
    lines = text.split('\n')
    pre_nums = []
    for line_num in range(len(lines)):
        match = re.finditer(r'[0-9]', lines[line_num])
        pre_nums.append([gap.span() for gap in match])

    for line_num in range(len(lines)):
        match = re.finditer(r'\*', lines[line_num])
        for gap in list(match):
            print(gap.span(), lines[line_num][gap.span()[0]])


print(part_1())
print(part_2())
