import Code.Game as game
from Code.AkariPuzzle import AkariPuzzle as ap
import numpy as np

def countPossibleNeighbourBulb(puzzle,row, col, cellType, probability_arr):
    counter = 0
    for x, y in ap.LIGHT_DIRECTION:
        if puzzle.isInBounds(row+y, col+x) and probability_arr[row+y, col+x] != -1 :
             if puzzle.arr[row+y, col+x] == cellType:
                counter+=1
    return counter

def checkProbability (puzzle, probability_arr):
    walls = np.where(np.logical_and(puzzle.arr >= 0, puzzle.arr <= 4))
    for row,col in zip(walls[0], walls[1]):
        probability_arr[row, col] = -1
        numBulb = puzzle.countNeighbour(row, col, ap.LIGHT_BULB)
        numLightOff = countPossibleNeighbourBulb(puzzle, row, col, ap.LIGHT_OFF,probability_arr)
        for x, y in ap.LIGHT_DIRECTION:
            temp_row, temp_col = row + y, col + x
            if puzzle.isInBounds(temp_row, temp_col) and puzzle.arr[temp_row, temp_col] == ap.LIGHT_OFF and  probability_arr[temp_row, temp_col] != -1:
                if puzzle.arr[row,col] <= numBulb or numLightOff == 0 :
                    probability_arr[temp_row, temp_col] = -1
                else:
                    probability_arr[temp_row, temp_col] = max(float(puzzle.arr[row,col]-numBulb)/float(numLightOff), probability_arr[temp_row, temp_col])
    return probability_arr

if __name__ == '__main__':
    f = game.read_puzzle_file()
    puzzle = game.get_next_puzzle(f)
    probability_arr = np.zeros((puzzle.rows, puzzle.cols), dtype=np.float64)
    puzzle.print_puzzle()
    probability_arr = checkProbability(puzzle, probability_arr)
    print(probability_arr)
    print()
    probability_arr = checkProbability(puzzle, probability_arr)

    # LightOffCell = np.where(puzzle.arr in range(5))

