# Artificial Intelligence_A1

COMP 4190
Artificial Intelligenc
Assignment 1

To run the program simply run the python code either for ForwardChecking.py or backtracking.py. 
If you want to test with heuristic, run the code which the file name format is <algorithm_Hn>. 

Backtracking: In this puzzle, the domain for each cell is no bulb and bulb, so the possible move is placing the bulb or
leaving blank. While one of the moves is legal, the algorithm would process recursively until the solution is found. 
Otherwise, do backtrack and keep going.

Backtracking_H1: H1 is Most Constrained Heuristic. Since backtrack algorithm does not track the domain for each cell, 
this heuristic is not available.

Backtracking_H2: This algorithm applies Most Constraining Heuristic. It places the light bulb to the cell that will 
impact the most unassigned cells. The priority is calculated by checking how many cells 
each bulb could light up. 

Backtracking_H3: Since H1 is not available, H3 (combination of H1 and H2) is the same as H2. 

Forward Checking:

Forward Checking H1:

Forward Checking H2:

Forward Checking H3: