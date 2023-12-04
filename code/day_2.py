import sys


def part_1():
    file = open('..\\input\\day_2.txt')
    sum = 0
    prep_arr = {'red': 12, 'green': 13, 'blue': 14}
    for line in file:
        arr_tmp = line.split(': ')
        game_num = int(arr_tmp[0].replace('Game ', ''))
        is_possible = True
        for game_try in arr_tmp[1].split('; '):
            for color_cubes in game_try.split(', '):
                for color in prep_arr.keys():
                    if color in color_cubes:
                        if int(color_cubes.split(' ')[0]) > prep_arr[color]:
                            is_possible = False
        if is_possible:
            sum = sum + game_num
    return sum


def part_2():
    file = open('..\\input\\day_2.txt')
    sum = 0
    for line in file:
        arr_tmp = line.split(': ')
        min_red = 0
        min_green = 0
        min_blue = 0
        for game_try in arr_tmp[1].split('; '):
            for color_cubes in game_try.split(', '):
                if 'red' in color_cubes:
                    new_value = int(color_cubes.split(' ')[0])
                    if new_value > min_red:
                        min_red = new_value
                elif 'green' in color_cubes:
                    new_value = int(color_cubes.split(' ')[0])
                    if new_value > min_green:
                        min_green = new_value
                else:
                    new_value = int(color_cubes.split(' ')[0])
                    if new_value > min_blue:
                        min_blue = new_value
        sum = sum + min_red * min_green * min_blue
    return sum


print(part_1())
print(part_2())
