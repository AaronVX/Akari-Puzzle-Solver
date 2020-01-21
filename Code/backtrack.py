import Code.Game as game
import numpy as np
import copy

counter = 0


def solvePuzzle(puzzle):
    domain = np.where(puzzle.arr == puzzle.LIGHT_OFF)
    if solvePuzzleUtil(puzzle, domain):
        print("**************")
        puzzle.print_puzzle()
        print("puzzle solved. \ntotal steps: {}".format(counter))
        return True
    else:
        print("solution doesn't exist")
        return False


def solvePuzzleUtil(puzzle_rec, domain):
    global counter
    if puzzle_rec.isFinished():
        return True

    if len(domain[0]) > 0:
        for row, col in zip(domain[0], domain[1]):
            counter += 1
            if puzzle_rec.isValidBulb(row, col) and puzzle_rec.isWallNeigbourValid(row, col):
                puzzle_rec.insert_light_bulb(row, col)
                domain = np.delete(domain, 0, 1)
                if solvePuzzleUtil(puzzle_rec, domain):
                    return True
                else:
                    puzzle_rec.removeLightBult(row, col)
                    np.insert(domain, 0, [row, col], axis=1)

    return False


if __name__ == '__main__':
    file = game.read_puzzle_file()
    puzzle = game.get_next_puzzle(file)
    # while puzzle.rows is not 8:
    #     puzzle = game.get_next_puzzle(file)
    puzzle2 = game.get_next_puzzle(file)
    puzzle3 = game.get_next_puzzle(file)
    puzzle4 = game.get_next_puzzle(file)
    puzzle5 = game.get_next_puzzle(file)
    puzzle5.print_puzzle()
    solvePuzzle(puzzle5)
