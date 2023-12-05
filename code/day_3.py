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


def part_2_v_1():
    sum = 0
    text = open('../input/day_3.txt').read()
    lines = text.split('\n')

    for line_num in range(len(lines)):
        match = re.finditer(r'\*', lines[line_num])
        for gap in list(match):
            if lines[line_num][gap.span()[0]] == '*':
                nums_with_gear = []
                if line_num - 1 >= 0:  # верх
                    left = gap.span()[0] - 3 if gap.span()[0] - 3 > 0 else 0
                    right = gap.span()[0] + 4 if gap.span()[0] + 4 < len(lines[line_num]) else len(lines[line_num]) - 1
                    substring = lines[line_num - 1][left:right]
                    nums_in_substr = re.finditer(r'\d+', substring)
                    little_left = 2 if gap.span()[0] - 1 >= 0 else 0
                    little_right = 4 if gap.span()[0] + 2 < len(lines[line_num]) else 2
                    for maybe_nums in list(nums_in_substr):
                        if ((maybe_nums.span()[0] >= little_left) != (maybe_nums.span()[1] <= little_right)) or \
                                (maybe_nums.span()[0] >= little_left and maybe_nums.span()[1] <= little_right):
                            nums_with_gear.append(int(substring[maybe_nums.span()[0]:maybe_nums.span()[1]]))

                if gap.span()[0] >= 0:  # лево
                    left = gap.span()[0] - 3 if gap.span()[0] - 3 > 0 else 0
                    substring = lines[line_num][left:gap.span()[0]]
                    nums_in_substr = re.finditer(r'\d+', substring)
                    nums_with_gear.append(int(nums_in_substr[-1]))

                if gap.span()[0] >= 0:  # право
                    pass
                if line_num + 1 < len(lines):  # низ
                    pass

            sum = sum + (nums_with_gear[0] * nums_with_gear[1])


def part_2_v_2():
    sum = 0
    text = open('../input/day_3.txt').read()
    lines = text.split('\n')
    vz_dict = {}
    for line_num in range(len(lines)):
        match = re.finditer(r'\d+', lines[line_num])
        for gap in list(match):
            is_valid = False
            num = int(lines[line_num][gap.span()[0]:gap.span()[1]])
            for i in range(gap.span()[0], gap.span()[1]):
                row = None
                col = None
                if line_num - 1 >= 0:
                    if re.match(r'\*', lines[line_num - 1][i]):  # верх
                        is_valid = True
                        row = line_num - 1
                        col = i
                if i + 1 < len(lines[line_num]):
                    if re.match(r'\*', lines[line_num][i + 1]):  # право
                        is_valid = True
                        row = line_num
                        col = i + 1
                if line_num + 1 < len(lines):
                    if re.match(r'\*', lines[line_num + 1][i]):  # низ
                        row = line_num + 1
                        col = i
                        is_valid = True
                if i - 1 >= 0:
                    if re.match(r'\*', lines[line_num][i - 1]):  # лево
                        row = line_num
                        col = i - 1
                        is_valid = True
                # диагонали
                if line_num - 1 >= 0 and i - 1 >= 0:
                    if re.match(r'\*', lines[line_num - 1][i - 1]):  # лево-верх
                        row = line_num - 1
                        col = i - 1
                        is_valid = True
                if line_num - 1 >= 0 and i + 1 < len(lines[line_num]):
                    if re.match(r'\*', lines[line_num - 1][i + 1]):  # право-верх
                        row = line_num - 1
                        col = i + 1
                        is_valid = True
                if line_num + 1 < len(lines) and i - 1 >= 0:
                    if re.match(r'\*', lines[line_num + 1][i - 1]):  # лево-низ
                        row = line_num + 1
                        col = i - 1
                        is_valid = True
                if line_num + 1 < len(lines) and i + 1 < len(lines[line_num]):
                    if re.match(r'\*', lines[line_num + 1][i + 1]):  # право-низ
                        row = line_num + 1
                        col = i + 1
                        is_valid = True
                if is_valid:
                    if (row, col) not in vz_dict.keys():
                        vz_dict[(row, col)] = []
                    vz_dict[(row, col)].append(num)
                    break
    for key in vz_dict.keys():
        if len(vz_dict.get(key)) > 1:
            sum = sum + vz_dict.get(key)[0] * vz_dict.get(key)[1]
    return sum




print(part_1())
print(part_2_v_2())
