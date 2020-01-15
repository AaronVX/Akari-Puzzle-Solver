from Code.puzzle import Puzzle

Puzzle_File_Name = "puzzle_sample/sample.txt"


def read_puzzle_file():
    print('Reading sample')
    f = open(Puzzle_File_Name, "r")
    return f


def next_puzzle(f):
    puzzle = []
    rows, cols = 0, 0

    if f is not None:
        line = f.readline()

        while line[0] is '#':
            line = f.readline()

        rows, cols = (int(s) for s in line.split())

        puzzle_str = [[1] * rows for g in range(cols)]

        for i in range(rows):
            cells = f.readline()
            for j in range(cols):
                if cells[j] is not '_':
                    puzzle[i][j] = int(cells[j])
                else:
                    puzzle[i][j] = 5

    return Puzzle(rows, cols, puzzle)


def create_puzzle(plzn):
    print('creating puzzle')


if __name__ == '__main__':
    f = read_puzzle_file()
    puzzle = next_puzzle(f)
    print(puzzle.str)
    f.close()
    print('done')
