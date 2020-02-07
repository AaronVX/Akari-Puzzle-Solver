# COMP 4190
# Authors:
#   Xiaojian Xie 7821950
# 	YanLam Ng 7775665
# Group: 9


import Code.Game as game
import numpy as np
import sys

counter = 0
# set HEURISTIC to true to enable backtracking with heuristic 2
HEURISTIC = True
DEBUG = True
checked_list = []
text_file = 'puzzle_sample/sample1.txt'


# count number of squares light up by the bulb
def countLightUp(puzzle, row, col):
    count = 0
    for x, y in puzzle.LIGHT_DIRECTION:
        col_temp, row_temp = col + x, row + y
        while puzzle.isInBounds(row_temp, col_temp):
            if puzzle.isLightBulb(row_temp, col_temp):
                break
            elif puzzle.isWall(row_temp, col_temp):
                break
            elif puzzle.arr[row_temp, col_temp] == puzzle.LIGHT_ON:
                count -= 1
            count += 1
            col_temp, row_temp = col_temp + x, row_temp + y
    return count


def solvePuzzle(puzzle):
    if HEURISTIC is False:
        notAssigned = np.where(puzzle.arr == puzzle.LIGHT_OFF)
        notAssigned_list = list(zip(notAssigned[0], notAssigned[1]))
    else:
        temp = np.where(puzzle.arr == puzzle.LIGHT_OFF)
        temp_list = list(zip(temp[0], temp[1]))
        notAssigned_list = findConstraining(puzzle, temp_list)

    if solvePuzzleUtil(puzzle, notAssigned_list):
        print("**************")
        puzzle.print_puzzle()
        print("puzzle solved. \ntotal number of nodes visited: {}".format(counter))
        return True
    else:
        print("solution doesn't exist")
        return False


def solvePuzzleUtil(puzzle_rec, notAssigned_list):
    global counter
    if puzzle_rec.isFinished():
        return True

    if counter > 100000:
        return "timeout"

    light_bulbs = np.where(puzzle_rec.arr == puzzle_rec.LIGHT_BULB)
    light_bulbs_list = list(zip(light_bulbs[0], light_bulbs[1]))

    if len(notAssigned_list) > 0 and light_bulbs_list not in checked_list: # avoid duplicate tracking
        for row, col in notAssigned_list:
            counter += 1
            temp = notAssigned_list.copy()
            temp.remove((row, col))
            if puzzle_rec.isValidBulb(row, col) and puzzle_rec.isWallNeigbourValid(row, col):
                puzzle_rec.insert_light_bulb(row, col)

                if DEBUG:
                    print("**************")
                    puzzle_rec.print_puzzle()
                    print(light_bulbs_list)
                if HEURISTIC and len(temp) > 0:
                    temp = findConstraining(puzzle_rec, temp)

                if solvePuzzleUtil(puzzle_rec, temp):
                    return True
                else:
                    puzzle_rec.removeLightBulb(row, col)
                    checked_list.append(light_bulbs_list)

    return False


def findConstraining(puzzle, notAssigned_list):
    if len(notAssigned_list) == 0:
        return []
    values = []
    for row, col in notAssigned_list:
        count = countLightUp(puzzle, row, col)
        # values.append([row, col, count * -1])
        values.append(tuple([row, col, count * -1]))

    dtype = [('row', int), ('col', int), ('range', int)]
    notAssigned_list_decending = np.array(values, dtype=dtype)
    notAssigned_list_decending = np.sort(notAssigned_list_decending, order=['range'])

    row_col_list = ['row', 'col']
    notAssigned_list_decending = notAssigned_list_decending[row_col_list]

    return list(map(tuple, notAssigned_list_decending))


if __name__ == '__main__':
    file = game.read_puzzle_file(text_file)
    puzzle = game.get_next_puzzle(file)
    # while puzzle.rows is not 8:
    #     puzzle = game.get_next_puzzle(file)
    # puzzle2 = game.get_next_puzzle(file)
    # puzzle3 = game.get_next_puzzle(file)
    # puzzle4 = game.get_next_puzzle(file)
    # puzzle5 = game.get_next_puzzle(file)
    puzzle.print_puzzle()
    solvePuzzle(puzzle)

    # checked_list = []
    # domain = np.where(puzzle.arr == puzzle.LIGHT_OFF)
    # print(domain)
    # findConstraining(puzzle, domain)


