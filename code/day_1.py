import re


def part_1():
    sum = 0
    f = open('../input/day_1.txt')
    for line in f:
        arr_letters = re.findall('[0-9]', line)
        print(arr_letters, int(arr_letters[0] + arr_letters[-1]))
        sum = sum + int(arr_letters[0] + arr_letters[-1])
    return sum


def part_2():
    sum = 0
    letter_dict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7',
                   'eight': '8', 'nine': '9'}
    pattern = r'(?=([0-9]'
    for key in letter_dict.keys():
        pattern = pattern + r'|' + key
    pattern = pattern + r'))'
    f = open('./input/day_1.txt')
    for line in f:
        arr_letters = re.findall(pattern, line)
        if arr_letters[0] in letter_dict:
            num_1 = letter_dict[arr_letters[0]]
        else:
            num_1 = arr_letters[0]
        if arr_letters[-1] in letter_dict:
            num_2 = letter_dict[arr_letters[-1]]
        else:
            num_2 = arr_letters[-1]
        print(sum, line, arr_letters, num_1 + num_2)
        sum = sum + int(num_1 + num_2)
    return sum


print(part_2())
