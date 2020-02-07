import Code.Game as game
import numpy as np

counter = 0
DEBUG = True
checked_list = []
text_file = 'puzzle_sample/sample.txt'


def solvePuzzle(puzzle):
    notAssigned = np.where(puzzle.arr == puzzle.LIGHT_OFF)
    notAssigned_list = list(zip(notAssigned[0], notAssigned[1]))

    if solvePuzzleUtil(puzzle, notAssigned_list):
        print("**************")
        puzzle.print_puzzle()
        print("puzzle solved. \ntotal steps: {}".format(counter))
        return True
    else:
        print("solution doesn't exist")
        return False


def solvePuzzleUtil(puzzle_rec, notAssigned_list):
    global counter
    if puzzle_rec.isFinished():
        return True

    light_bulbs = np.where(puzzle_rec.arr == puzzle_rec.LIGHT_BULB)
    light_bulbs_list = list(zip(light_bulbs[0], light_bulbs[1]))

    if len(notAssigned_list) > 0 and light_bulbs_list not in checked_list:
        for row, col in notAssigned_list:
            counter += 1
            if puzzle_rec.isValidBulb(row, col) and puzzle_rec.isWallNeigbourValid(row, col):
                puzzle_rec.insert_light_bulb(row, col)
                temp = notAssigned_list.copy()
                temp.remove((row, col))

                if DEBUG:
                    print("**************")
                    puzzle_rec.print_puzzle()
                    # print(temp)

                if solvePuzzleUtil(puzzle_rec, temp):
                    return True
                else:
                    puzzle_rec.removeLightBulb(row, col)
                    checked_list.append(light_bulbs_list)

    return False

if __name__ == '__main__':
    file = game.read_puzzle_file(text_file)
    puzzle = game.get_next_puzzle(file)
    while puzzle.rows is not 8:
        puzzle = game.get_next_puzzle(file)
    puzzle2 = game.get_next_puzzle(file)
    puzzle3 = game.get_next_puzzle(file)
    puzzle4 = game.get_next_puzzle(file)
    puzzle5 = game.get_next_puzzle(file)
    puzzle4.print_puzzle()
    solvePuzzle(puzzle4)





