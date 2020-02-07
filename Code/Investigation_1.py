# COMP 4190
# Authors:
#   Xiaojian Xie 7821950
# 	YanLam Ng 7775665
# Group: 9

import Code.Game as game
from Code.AkariPuzzle import AkariPuzzle as ap
import Code.ForwardChecking as fc
import Code.Forward_H1 as fc_H1
import Code.Forward_H2 as fc_H2
import Code.Forward_H3 as fc_H3
import numpy as np
from termcolor import colored
import Code.ForwardChecking as fc

DEBUG = False
counter = 0
checked_set = []
testing_file_name = 'puzzle_sample/lightup puzzles.txt'


if __name__ == '__main__':
    f = game.read_puzzle_file(fileName=testing_file_name)
    puzzle = game.get_next_puzzle(f, isForward=True)

    while puzzle is not None:
        fc.solvePuzzle(puzzle)
        fc_H1.solvePuzzle(puzzle)
        fc_H2.solvePuzzle(puzzle)
        fc_H3.solvePuzzle(puzzle)
        puzzle = game.get_next_puzzle(f, isForward=True)



