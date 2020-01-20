import Code.Game as game
import numpy as np
import copy

counter = 0
DEBUG = True

def solvePuzzle(puzzle5):
    if solvePuzzleUtil(puzzle5):
        puzzle5.print_puzzle()
        print("puzzle solved. \ntotal steps: {}".format(counter))
        return True
    else:
        print("solution doesn't exist")
        return False


def solvePuzzleUtil(puzzle_rec):
    global counter
    if puzzle_rec.isFinished():
        return True

    lightBulbs = np.where(puzzle_rec.arr == puzzle_rec.LIGHT_OFF)

    if len(lightBulbs[0]) > 0:
        for row, col in zip(lightBulbs[0], lightBulbs[1]):
            if puzzle_rec.isValidBulb(row, col) and puzzle_rec.isWallNeigbourValid(row, col):
                puzzle_rec.insert_light_bulb(row, col)
                counter += 1
                if DEBUG: puzzle_rec.print_puzzle()
                if DEBUG: print("****************")
                if solvePuzzleUtil(puzzle_rec):
                    return True
                else:
                    puzzle_rec.removeLightBult(row, col)
    return False


if __name__ == '__main__':
    file = game.read_puzzle_file()
    puzzle = game.get_next_puzzle(file)
    puzzle2 = game.get_next_puzzle(file)
    puzzle3 = game.get_next_puzzle(file)
    puzzle4 = game.get_next_puzzle(file)
    puzzle5 = game.get_next_puzzle(file)
    puzzle5.print_puzzle()
    solvePuzzle(puzzle5)
