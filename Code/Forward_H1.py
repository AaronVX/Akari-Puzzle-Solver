import Code.Game as game
from Code.AkariPuzzle import AkariPuzzle as ap
import numpy as np
from termcolor import colored
import Code.ForwardChecking as fc

DEBUG = False
counter = 0
checked_set = []


def solvePuzzleH1(puzzle5):
    global counter, checked_set
    counter = 0
    checked_set = []
    if solvePuzzleUtil_H1(puzzle5,np.copy(puzzle5.probability_arr)):
        print("**************")
        puzzle5.print_puzzle()
        print("puzzle solved. \ntotal steps: {}".format(counter))
        return True
    else:
        print("solution doesn't exist")
        return False



def solvePuzzleUtil_H1(puzzle_rec,probability_arr):
    global counter,checked_set
    if puzzle_rec.isFinished():
        return True

    fc.update_constraint(puzzle_rec, probability_arr)
    possible_cell = np.where(probability_arr >= 0)
    light_off_bulbs = np.where(puzzle_rec.arr == puzzle_rec.LIGHT_OFF)
    possible_cell_set = set(zip(possible_cell[0], possible_cell[1])).intersection(set(zip(light_off_bulbs[0], light_off_bulbs[1])))
    possible_cell_set = sorted(possible_cell_set, key=lambda cell: probability_arr[cell[0], cell[1]], reverse=True)
    light_bulbs = np.where(puzzle_rec.arr == puzzle_rec.LIGHT_BULB)
    light_bulbs_set = set(zip(light_bulbs[0], light_bulbs[1]))
    if len(possible_cell[0]) > 0:
        for row, col in possible_cell_set:
            counter += 1
            if puzzle_rec.isValidBulb(row, col) and puzzle_rec.isWallNeigbourValid(row, col) and light_bulbs_set.union({(row,col)}) not in checked_set:
                puzzle_rec.insert_light_bulb(row, col)
                fc.check_cell_lightup_constraint(puzzle_rec, probability_arr,row,col)
                next_probability_arr = np.copy(probability_arr)
                next_probability_arr[row, col] = -1
                if DEBUG: puzzle_rec.print_puzzle()
                if DEBUG: print("****************")
                # if DEBUG: print_probability_arr(next_probability_arr)

                if solvePuzzleUtil_H1(puzzle_rec, next_probability_arr):
                    return True
                else:
                    puzzle_rec.removeLightBult(row, col)
                    if DEBUG: puzzle_rec.print_puzzle()
                    checked_set.append(light_bulbs_set)
    return False

if __name__ == '__main__':
    f = game.read_puzzle_file(fileName="puzzle_sample/sample.txt")
    puzzle = game.get_next_puzzle(f, isForward=True)

    while puzzle is not None:
        puzzle.print_solution()
        solvePuzzleH1(puzzle)
        # print_constraited_puzzle(puzzle)
        puzzle = game.get_next_puzzle(f, isForward=True)
    # LightOffCell = np.where(puzzle.arr in range(5))


