# sudokuSolver
Sudoku Solver using Backtracking Algorithm. Implementing Turtle module to represent how th sudoku board and how the algorithm works.

To this date, this project needs two files to run. One file called SudokuSolver.py, that will take care of how the algorithm works to find a solution.
The other file, called SudokuBuilder.py, uses Turtle module from python to build an internal representation of the sudoku table, and to see "live" how
the backtracking algorithm builds the solution. 

Note, that SudokuSolve.py imports the file to make the internal representation, and take care of the details.
Only thing is required to run the program is to create an instance of SudokeSolver class, that will take an array representing the board as a parameter.
Once the instance is created, we need to execute the function .getSolution() of that instance. The program will do the rest.

For testing purposes, the file already contains an array of an unsolved sudoku. In future updates, I will work on make some comments on the SudokuBuilder.py
file, for those more insterested on how the visual aspect works. 

Hope you enjoy it!
