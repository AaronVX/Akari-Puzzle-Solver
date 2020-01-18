from Code.AkariPuzzle import AkariPuzzle
import numpy as np

Puzzle_File_Name = "puzzle_sample/sample.txt"


def read_puzzle_file():
    print('Reading sample')
    f = open(Puzzle_File_Name, "r")
    return f


def get_next_puzzle(f):
    puzzle = None
    rows, cols = 0, 0

    if f is not None:
        line = f.readline()

        while line[0] is '#':
            line = f.readline()

        rows, cols = (int(s) for s in line.split())

        puzzle = np.zeros((rows, cols), dtype=np.int8)

        for i in range(rows):
            cells = f.readline()
            for j in range(cols):
                if cells[j] is '_':
                    puzzle[i, j] = AkariPuzzle.LIGHT_OFF
                else:
                    puzzle[i, j] = int(cells[j])

    return AkariPuzzle(rows, cols, puzzle)



if __name__ == '__main__':
    f = read_puzzle_file()

    puzzle = get_next_puzzle(f)
    while not puzzle.isFinished():
        puzzle.print_puzzle()
        mode = int(input('\nSelect mode:\n0 ==> insert light bulb\n1 ==> delete light bulb\n'))
        if mode == 0:
            row = int(input('Enter the row of light bulb: '))
            col = int(input('Enter the col of light bulb: '))
            if not puzzle.insert_light_bulb(row, col):
                print('fail to insert')
        elif mode == 1:
            row = int(input('Enter the row of light bulb: '))
            col = int(input('Enter the col of light bulb: '))
            if not puzzle.removeLightBult(row, col):
                print('fail to remove')
        print('/********************/\n')

    f.close()
    print('done')
