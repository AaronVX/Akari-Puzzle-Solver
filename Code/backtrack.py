import Code.Game as game
import numpy as np
import copy

counter = 0

checked_set = []

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
    # puzzle_rec.print_puzzle()

    if puzzle_rec.isFinished():
        return True
    light_bulbs = np.where(puzzle_rec.arr == puzzle_rec.LIGHT_BULB)
    light_bulbs_set = set(zip(light_bulbs[0], light_bulbs[1]))

    if len(domain[0]) > 0 and light_bulbs_set not in checked_set:
        domain_set =  zip(domain[0], domain[1])
        for row, col in domain_set:
            counter += 1
            if puzzle_rec.isValidBulb(row, col) and puzzle_rec.isWallNeigbourValid(row, col):
                puzzle_rec.insert_light_bulb(row, col)
                domain = np.delete(domain, 0, 1)
                if solvePuzzleUtil(puzzle_rec, domain):
                    return True
                else:
                    puzzle_rec.removeLightBult(row, col)
                    np.insert(domain, 0, [row, col], axis=1)

                    # puzzle_rec.print_puzzle()
                    checked_set.append(light_bulbs_set)
    return False

if __name__ == '__main__':
    file = game.read_puzzle_file()
    puzzle = game.get_next_puzzle(file)
    # while puzzle.rows is not 8:
    #     puzzle = game.get_next_puzzle(file)
    puzzle2 = game.get_next_puzzle(file)
    puzzle3 = game.get_next_puzzle(file)
    puzzle4 = game.get_next_puzzle(file)
    puzzle = game.get_next_puzzle(file)

    solvePuzzle(puzzle)
