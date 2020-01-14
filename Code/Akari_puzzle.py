from Code.puzzle import Puzzle

Puzzle_File_Name = "puzzle_sample/sample.txt"



def read_puzzle_file():
    print('Reading sample')
    f = open(Puzzle_File_Name, "r")
    return f


def next_puzzle(f):
    puzzle_str = ''
    rows, cols = 0, 0

    if f is not None:
        line = f.readline()

        while line[0] is '#':
            line = f.readline()

        rows, cols = (int(s) for s in line.split())

        for i in range(rows):
            puzzle_str += f.readline()

    return Puzzle(rows, cols, puzzle_str)


def create_puzzle(plzn):
    print('creating puzzle')

if __name__ == '__main__':
    f = read_puzzle_file()
    puzzle = next_puzzle(f)
    print(puzzle.str)
    f.close()
    print('done')
