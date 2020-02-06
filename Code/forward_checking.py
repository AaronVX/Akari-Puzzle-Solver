import Code.Game as game
import numpy as np
import copy

counter = 0


def solvePuzzle(puzzle5):
    if solvePuzzleUtil(puzzle5):
        print("**************")
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

    light_off_bulbs = np.where(puzzle_rec.arr == puzzle_rec.LIGHT_OFF)

    if len(light_off_bulbs[0]) > 0:
        for row, col in zip(light_off_bulbs[0], light_off_bulbs[1]):
            counter += 1
            if puzzle_rec.isValidBulb(row, col) and puzzle_rec.isWallNeigbourValid(row, col):
                puzzle_rec.insert_light_bulb(row, col)

                # puzzle_rec.print_puzzle()
                # print("****************")
                if solvePuzzleUtil(puzzle_rec):
                    return True
                else:
                    puzzle_rec.removeLightBulb(row, col)
    return False


if __name__ == '__main__':
    file = game.read_puzzle_file()
    puzzle = game.get_next_puzzle(file)
    # while puzzle.rows is not 10:
    #     puzzle = game.get_next_puzzle(file)

    puzzle.print_puzzle()
    solvePuzzle(puzzle)
