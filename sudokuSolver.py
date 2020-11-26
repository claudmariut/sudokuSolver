import numpy as np
from sudokuBuilder import SudokuDraw, turtle


class SudokuSolver:
    """Sudoku Solver"""

    def __init__(self, sudoku):
        self.sudoku = sudoku
        self.emptyPlaces = []
        self.solutionNode = []
        self.setEmptyPlaces()  # Crete list with coordinates of empty spots.
        self.s = SudokuDraw()
        self.drawSudoku()

    def drawSudoku(self):
        """Representation of the Sudoku."""
        self.s.wn.tracer(0)
        for row in range(9):
            for column in range(9):
                if self.sudoku[row][column] != 0:
                    num = self.sudoku[row][column]
                    self.s.writeCellSudoku(num, row, column)

    def setEmptyPlaces(self):
        """Find empty places in the sudoku and store them."""
        for row in range(9):
            for column in range(9):
                if self.sudoku[row][column] == 0:
                    self.emptyPlaces.append((row, column))

    def getEmptyPlaces(self):
        """Return empty places."""
        return self.emptyPlaces

    def getNodeValue(self, node):
        """Return Value of the Node"""
        return self.sudoku[node[0]][node[1]]

    def setNodeValue(self, node, value):
        """Set the value of a node."""
        row = node[0]
        column = node[1]
        self.sudoku[row][column] = value
        self.s.writeCellSudoku(value, row, column)

    def getBox(self, node):
        """Get box array of a given node from sudoku."""
        row = node[0]
        column = node[1]
        if row in (0, 1, 2):
            if column in (0, 1, 2):
                return self.sudoku[0:3, 0:3]
            elif column in (3, 4, 5):
                return self.sudoku[0:3, 3:6]
            elif column in (6, 7, 8):
                return self.sudoku[0:3, 6:9]
        elif row in (3, 4, 5):
            if column in (0, 1, 2):
                return self.sudoku[3:6, 0:3]
            elif column in (3, 4, 5):
                return self.sudoku[3:6, 3:6]
            elif column in (6, 7, 8):
                return self.sudoku[3:6, 6:9]
        elif row in (6, 7, 8):
            if column in (0, 1, 2):
                return self.sudoku[6:9, 0:3]
            elif column in (3, 4, 5):
                return self.sudoku[6:9, 3:6]
            elif column in (6, 7, 8):
                return self.sudoku[6:9, 6:9]

    def getConstraints(self, node, value):
        """Return true if value fits in node."""
        row = node[0]
        column = node[1]
        if value not in self.sudoku[row] \
                and value not in self.sudoku[:, column]:
            if value not in self.getBox(node):
                return True
        else:
            return False

    def resetNode(self, node):
        """Reset the node value to 0 when Backtracking."""
        row = node[0]
        column = node[1]
        self.sudoku[row][column] = 0
        self.s.resetCellSudoku(row, column)

    def getSolution(self):
        """Build solution nodes using Backtracking"""
        place = 0
        while True:
            node = self.emptyPlaces[place]
            value = self.getNodeValue(node)
            while True:
                if value < 9:
                    value += 1
                    if self.getConstraints(node, value):
                        self.setNodeValue(node, value)
                        self.solutionNode.append(value)
                        place += 1
                        break
                elif value == 9:
                    self.resetNode(node)
                    self.solutionNode.pop()
                    place -= 1
                    break
            if node == self.emptyPlaces[-1]:
                break
        return self.sudoku


sudoku = np.array([[0, 0, 0, 0, 3, 0, 0, 0, 0],
                   [0, 0, 1, 0, 7, 6, 9, 4, 0],
                   [0, 8, 0, 9, 0, 0, 0, 0, 0],
                   [0, 4, 0, 0, 0, 1, 0, 0, 0],
                   [0, 2, 8, 0, 9, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 1, 6, 0],
                   [7, 0, 0, 8, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 4, 0, 2],
                   [0, 9, 0, 0, 1, 0, 3, 0, 0]])

puzzle1 = SudokuSolver(sudoku)
puzzle1.getSolution()
puzzle1.s.wn.exitonclick()
