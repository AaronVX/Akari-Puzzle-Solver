import Code.Game as game
from Code.AkariPuzzle import AkariPuzzle as ap
import numpy as np
from termcolor import colored
import os

DEBUG = True
counter = 0
checked_set = []
def countPossibleNeighbourBulb(puzzle,probability_arr,row, col, cellType):
    bulbs_counter = 0
    certain_bulb = 0
    for x, y in ap.LIGHT_DIRECTION:
        if puzzle.isInBounds(row+y, col+x):
            if probability_arr[row+y, col+x] == 1:
                certain_bulb += 1
            elif probability_arr[row+y, col+x] != -1:
                 if puzzle.arr[row+y, col+x] == cellType:
                    bulbs_counter+=1
    return bulbs_counter, certain_bulb

def check_wall_constraint(puzzle,probability_arr, row, col):
    probability_arr[row, col] = -1
    numBulb = puzzle.countNeighbour(row, col, ap.LIGHT_BULB)

    numLightOff, certain_bulb = countPossibleNeighbourBulb(puzzle,probability_arr, row, col, ap.LIGHT_OFF)
    numBulb += certain_bulb
    for x, y in ap.LIGHT_DIRECTION:
        temp_row, temp_col = row + y, col + x
        if puzzle.isInBounds(temp_row, temp_col) and puzzle.arr[temp_row, temp_col] == ap.LIGHT_OFF and probability_arr[
            temp_row, temp_col] != -1 and probability_arr[temp_row, temp_col] != 1:
            if puzzle.arr[row, col] <= numBulb or numLightOff == 0:
                probability_arr[temp_row, temp_col] = -1
                check_neighbour_constraint(puzzle, probability_arr, row, col)
            else:
                probability_arr[temp_row, temp_col] = float(puzzle.arr[row, col] - numBulb) / float(numLightOff)
                if probability_arr[temp_row, temp_col] == 1:
                    check_cell_lightup_constraint(puzzle, probability_arr, temp_row, temp_col)


# def checkProbability (puzzle):
#     walls = np.where(np.logical_and(puzzle.arr >= 0, puzzle.arr <= 4))
#     for row,col in zip(walls[0], walls[1]):
#         check_wall_constraint(puzzle, row, col)



# def light_up_constraint(puzzle,probability_arr):
#     certain_bulb_indexes = np.where(puzzle.arr == puzzle.LIGHT_BULB)
#     certain_bulb_position = set(zip(certain_bulb_indexes[0], certain_bulb_indexes[1]))
#     certain_bulb_indexes = np.where(probability_arr == 1)
#     certain_bulb_position |= set(zip(certain_bulb_indexes[0], certain_bulb_indexes[1]))
#     for row, col in certain_bulb_position:
#         check_cell_lightup_constraint(puzzle,row,col)
def check_neighbour_constraint(puzzle,probability_arr,row,col):
    for x, y in ap.LIGHT_DIRECTION:
        col_temp, row_temp = col + x, row + y
        if puzzle.isInBounds(row_temp, col_temp) and puzzle.isWall(row_temp, col_temp):
            if (row_temp, col_temp) not in puzzle.update_list:
                puzzle.update_list.append((row_temp, col_temp))

def check_cell_lightup_constraint(puzzle,probability_arr,row,col):
    for x, y in ap.LIGHT_DIRECTION:
        neigbour = []
        if y == 0:
            neigbour =[(0,1), (0,-1)]
        elif x == 0:
            neigbour = [(1,0), (-1, 0)]
        col_temp, row_temp = col + x, row + y
        while puzzle.isInBounds(row_temp, col_temp):
            if puzzle.isWall(row_temp, col_temp) :
                puzzle.update_list.append(( row_temp,col_temp))
                break
            elif puzzle.isLightBulb(row_temp, col_temp):
                break
            else:
                probability_arr[row_temp, col_temp] = -1
                for neigbour_x, neigbour_y in neigbour:
                    row_neigbour, col_neigbour = row_temp + neigbour_y, col_temp + neigbour_x
                    if puzzle.isWall(row_neigbour, col_neigbour):
                        puzzle.update_list.append((row_neigbour, col_neigbour))

            col_temp, row_temp = col_temp + x, row_temp + y
    return True  # insert successfully

def updade_neigbour(puzzle, row, col):
    for x, y in ap.LIGHT_DIRECTION:
        col_temp, row_temp = col + x, row + y
        while puzzle.isInBounds(row_temp, col_temp):
            if puzzle.isWall(row_temp, col_temp):
                puzzle.update_position_set |= (row_temp, col_temp)

            col_temp, row_temp = col_temp + x, row_temp + y
    return True  # insert successfully

def print_constraited_puzzle(probability_arr):
    print('/*******************************************/')
    for i in range(puzzle.rows):
        for j in range(puzzle.cols):
            value = probability_arr[i, j]
            if value == -1:
                print(colored('X', 'red'), end=' ')
            elif value == 1:
                print(colored('b', 'green'), end=' ')
            else:
                print(colored('_', 'blue'), end=' ')
        print()
    print()


def update_constraint(puzzle,probability_arr):
    while len(puzzle.update_list) > 0:
        update_cell_y, update_cell_x  = puzzle.update_list.pop(0)
        check_wall_constraint(puzzle,probability_arr, update_cell_y,update_cell_x)
        num_zeros = (probability_arr == -1).sum()
        num_ones = (probability_arr == 1).sum()
        if num_zeros + num_ones == puzzle.rows * puzzle.cols:
            break



def solvePuzzle(puzzle5):
    global counter, checked_set
    counter = 0
    checked_set = []
    if solvePuzzleUtil(puzzle5,np.copy(puzzle5.probability_arr)):
        print("**************")
        puzzle5.print_puzzle()
        print("puzzle solved. \ntotal steps: {}".format(counter))
        return True
    else:
        print("solution doesn't exist")
        return False


def print_probability_arr(probability_arr):
    for row in probability_arr:
        for value in row:
            if value < 0:
                print(colored(value, 'red'), end=' ')
            else:
                print(colored(' '+str(value), 'green'), end=' ')
        print()



def solvePuzzleUtil(puzzle_rec,probability_arr):
    global counter,checked_set
    if puzzle_rec.isFinished():
        return True

    update_constraint(puzzle_rec, probability_arr)
    possible_cell = np.where(probability_arr >= 0)
    #light_off_bulbs = np.where(puzzle_rec.arr == puzzle_rec.LIGHT_OFF)
    possible_cell_set = set(zip(possible_cell[0], possible_cell[1]))#.intersection(set(zip(light_off_bulbs[0], light_off_bulbs[1])))

    light_bulbs = np.where(puzzle_rec.arr == puzzle_rec.LIGHT_BULB)
    light_bulbs_set = set(zip(light_bulbs[0], light_bulbs[1]))
    if len(possible_cell[0]) > 0:
        for row, col in possible_cell_set:
            counter += 1

            print("step: {0}".format(str(counter)))

            if puzzle_rec.isValidBulb(row, col) and puzzle_rec.isWallNeigbourValid(row, col) and light_bulbs_set.union({(row,col)}) not in checked_set:
                puzzle_rec.insert_light_bulb(row, col)
                check_cell_lightup_constraint(puzzle_rec, probability_arr,row,col)
                next_probability_arr = np.copy(probability_arr)
                next_probability_arr[row, col] = -1
                if DEBUG: puzzle_rec.print_puzzle()
                if DEBUG: print("****************")
                # if DEBUG: print_probability_arr(next_probability_arr)

                if solvePuzzleUtil(puzzle_rec, next_probability_arr):
                    return True
                else:
                    puzzle_rec.removeLightBult(row, col)
                    if DEBUG: puzzle_rec.print_puzzle()
                    checked_set.append(light_bulbs_set)
    return False

if __name__ == '__main__':
    f = game.read_puzzle_file(fileName="puzzle_sample/sample1.txt")
    puzzle = game.get_next_puzzle(f, isForward=True)

    while puzzle is not None:
        puzzle.print_solution()
        solvePuzzle(puzzle)
        # print_constraited_puzzle(puzzle)
        puzzle = game.get_next_puzzle(f, isForward=True)
    # LightOffCell = np.where(puzzle.arr in range(5))


