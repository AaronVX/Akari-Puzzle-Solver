
class Cell:

    def __init__(self, row, col):
        self.col = col
        self.row = row


class Wall(Cell):
    def __init__(self, row, col, num):
        Cell.__init__(self, row, col)
        self.num = num
        print(num)

class EmptyCell(Cell):
    def __init__(self, row, col, isLightUp = False):
        Cell.__init__(self, row, col)
        self.isLightUp = isLightUp


class Puzzle:
    puzzle = [[1] * 8 for i in range(8)]

    def __init__(self, rows, cols, puzzle_str):
        self.cols = cols
        self.rows = rows
        self.str = puzzle_str
        self.puzzle_solution = None


    # not done yet
    # def str2puzzle(self):
    #     for row_num, row_str in enumerate(self.str.split("\n")):
    #
    #         for col_num, ch in enumerate(row_str):
    #             cell = None
    #             if ch.isdigit():
    #                 cell = Wall(row_num, col_num, int(ch))
    #             else:
    #                 cell = EmptyCell(row_num, col_num, False)
    #
    #
    #
