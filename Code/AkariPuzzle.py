import numpy as np


# puzzle cell value
# 0-4 = wall
# 5 = no light
# 6 = light up
# 7 = light bulb


class AkariPuzzle:
    LIGHT_DIRECTION = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    LIGHT_OFF = 5
    LIGHT_ON = 6
    LIGHT_BULB = 7

    def __init__(self, rows, cols, puzzle_arr):
        self.cols = cols
        self.rows = rows
        self.original_puzzle = puzzle_arr
        self.arr = puzzle_arr.copy()

    # check the position whether is on the pazzle
    def isInBounds(self, row, col):
        if col >= 0 and col < self.cols and row >= 0 and row < self.rows:
            return True
        return False

    def isWall(self, row, col):
        if self.arr[row, col] in range(5):
            return True
        return False

    def isLightBulb(self, row, col):
        if self.arr[row, col] == AkariPuzzle.LIGHT_BULB:
            return True
        return False

    def removeLightBult(self, row, col):
        if self.isInBounds(row, col) and self.isLightBulb(row, col):
            self.arr[row, col] = AkariPuzzle.LIGHT_OFF
            self.update_puzzle()
            return True  # remove successfully
        return False  # failure

    def insert_light_bulb(self, row, col):
        if self.isInBounds(row, col) and self.isWall(row, col) is False:
            self.arr[row, col] = AkariPuzzle.LIGHT_BULB

            for x, y in AkariPuzzle.LIGHT_DIRECTION:
                col_temp, row_temp = col + x, row + y
                while self.isInBounds(row_temp, col_temp):
                    if self.isWall(row_temp, col_temp) or self.isLightBulb(row_temp, col_temp):
                        break
                    else:
                        self.arr[row_temp, col_temp] = AkariPuzzle.LIGHT_ON

                    col_temp, row_temp = col_temp + x, row_temp + y
            return True  # insert successfully
        return False

    # return the number of light bulb neigbour cell(up, down, left, right)
    def countNeigbourBulb(self, row, col):
        counter = 0
        for x, y in AkariPuzzle.LIGHT_DIRECTION:
            if self.isInBounds(row + y, col + x):
                if self.arr[row + y, col + x] == AkariPuzzle.LIGHT_BULB:
                    counter += 1
        return counter

    # check there is no double light bulb in same row or same col
    def isValidBulb(self, row, col):

        for x, y in AkariPuzzle.LIGHT_DIRECTION:
            col_temp, row_temp = col + x, row + y
            while self.isInBounds(row_temp, col_temp):
                if self.isLightBulb(row_temp, col_temp):
                    return True
                elif self.isWall(row_temp, col_temp):
                    break
                col_temp, row_temp = col_temp + x, row_temp + y
        return False

    # check whether the wall has correct number of neigbouring bulbs
    def isWallNeigbourValid(self, row, col):
        for x, y in AkariPuzzle.LIGHT_DIRECTION:
            if self.isInBounds(row + y, col + x):
                if self.arr[row + y, col + x] <= 4:
                    if self.arr[row + y, col + x] == self.countNeigbourBulb(row + y, col + x):
                        return False
        return True

    # update the light off cell after removing a lightbulb cell
    def update_puzzle(self):
        bulb_indexes = np.where(self.arr == AkariPuzzle.LIGHT_BULB)
        self.arr = self.original_puzzle.copy()
        for row, col in zip(bulb_indexes[0], bulb_indexes[1]):
            self.insert_light_bulb(row, col)

    # whether the win condition is match
    def isFinished(self):
        isAllLightOn = False
        isWallNeigbourValid = True
        isNoDoubleBulb = True
        if len(np.where(self.arr == AkariPuzzle.LIGHT_OFF)[0]) == 0:  # no light OFF cell
            isAllLightOn = True

        wall_indexes = np.where(self.arr <= 4)
        for row, col in zip(wall_indexes[0], wall_indexes[1]):
            if self.arr[row, col] != self.countNeigbourBulb(row, col):
                isWallNeigbourValid = False
                break

        lightBulbs = np.where(self.arr == AkariPuzzle.LIGHT_BULB)
        for row, col in zip(lightBulbs[0], lightBulbs[1]):
            if self.isValidBulb(row, col):
                isNoDoubleBulb = False
                break

        return isAllLightOn and isWallNeigbourValid and isNoDoubleBulb

    def to_s(self):
        str = ''
        for i in range(self.rows):
            for j in range(self.cols):
                value = self.arr[i, j]
                if value in range(5):
                    str += self.arr[i][j]
                elif value == AkariPuzzle.LIGHT_OFF:
                    str += '_'
                elif value == AkariPuzzle.LIGHT_ON:
                    str += '#'
                elif value == AkariPuzzle.LIGHT_BULB:
                    str += 'b'
            str += '\n'

    def print_puzzle(self):
        for i in range(self.rows):
            for j in range(self.cols):
                value = self.arr[i, j]
                if value in range(5):
                    print(self.arr[i][j], end=' ')
                elif value == AkariPuzzle.LIGHT_OFF:
                    print('_', end=' ')
                elif value == AkariPuzzle.LIGHT_ON:
                    print('#', end=' ')
                elif value == AkariPuzzle.LIGHT_BULB:
                    print('b', end=' ')
            print()
