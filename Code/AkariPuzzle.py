import numpy as np
#puzzle cell value
# 0-4 = wall
# 5 = no light
# 6 = light up
# 7 = light bulb
LIGHT_OFF = 5
LIGHT_ON = 6
LIGHT_BULB = 7



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

    #check the position whether is on the pazzle
    def isInBounds(self, row, col):
        if col >= 0 and col < self.cols and row >= 0 and row < self.rows :
            return True
        return False

    def isWall(self, row, col):
        if self.arr[row, col] in range(5):
            return True
        return False


    def isLightBulb(self, row, col):
        if self.arr[row,col] == LIGHT_BULB:
            return True
        return False

    def removeLightBult(self,row, col):
        if self.isInBounds(row, col) and self.isLightBulb(row, col):
            self.arr[row,col] = LIGHT_OFF
            self.update_puzzle()
            return True         #remove successfully
        return False            #failure


    def insert_light_bulb(self, row, col):
        if self.isInBounds(row, col) and self.isWall(row,col) is False:
            self.arr[row, col] = LIGHT_BULB
            theRow = self.arr[row,:]
            theCol = self.arr[:, col]

            for x, y in AkariPuzzle.LIGHT_DIRECTION:
                col_temp, row_temp = col + x, row + y
                while self.isInBounds(row_temp, col_temp):
                    if self.isWall(row_temp, col_temp) or self.isLightBulb(row_temp, col_temp):
                        break
                    else:
                        self.arr[row_temp, col_temp] = LIGHT_ON

                    col_temp, row_temp = col_temp + x, row_temp + y
            return True         #insert successfully
        return False


    def print_puzzle(self):
        for i in range(self.rows) :
            for j in range(self.cols):
                value = self.arr[i,j]
                if value in range(5):
                    print(self.arr[i][j], end = ' ')
                elif value == LIGHT_OFF:
                    print('_', end = ' ')
                elif value == LIGHT_ON:
                    print('#', end = ' ')
                elif value == LIGHT_BULB:
                    print('b', end = ' ')
            print()

    def countNeigbourBulb(self, row, col):

        counter = 0
        for x, y in AkariPuzzle.LIGHT_DIRECTION:
            if self.isInBounds(row+y, col+x):
                 if self.arr[row+y, col+x] == LIGHT_BULB:
                    counter+=1
        return counter

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


    def update_puzzle(self):
        bulb_indexes = np.where(self.arr == LIGHT_BULB)
        self.arr = self.original_puzzle.copy()
        for row, col in zip(bulb_indexes[0],bulb_indexes[1]) :
            self.insert_light_bulb(row, col)



    def isFinished(self):
        isAllLightOn = False
        isWallNeigbourValid = True
        isNoDoubleBulb = True
        if len(np.where(self.arr == LIGHT_OFF)[0]) == 0: #no light OFF cell
            isAllLightOn = True

        wall_indexes = np.where(self.arr <= 4)
        for row, col in zip(wall_indexes[0], wall_indexes[1]):
            if self.arr[row, col] != self.countNeigbourBulb(row, col):
                isWallNeigbourValid = False
                break

        lightBulbs = np.where(self.arr == LIGHT_BULB)
        for row, col in zip(lightBulbs[0], lightBulbs[1]):
            if self.isValidBulb(row, col):
                isNoDoubleBulb = False
                break

        return isAllLightOn and isWallNeigbourValid and isNoDoubleBulb