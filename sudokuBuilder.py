import turtle


class SudokuDraw:
    """Represent a sudoku drawing."""
    def __init__(self):
        self.s = turtle.Turtle()
        self.wn = turtle.Screen()
        self.wn.setup(width=800, height=800)
        self.wn.setworldcoordinates(0, 0, 9, 9)
        self.wn.colormode(255)
        self.drawSudoku()
        self.sudokuDic = {}


    def drawSudoku(self):
        self.s.hideturtle()
        self.wn.tracer(0)
        self.s.goto(0, 0)
        self.s.pensize(5)
        self.s.begin_fill()
        for i in range(4):
            self.s.fillcolor((184, 220, 213))
            self.s.forward(9)
            self.s.left(90)
        self.s.end_fill()

        for i in range(1, 9):
            self.s.up()
            self.s.goto(0, i)
            self.s.down()
            if i == 3 or i == 6:
                self.s.pensize(5)
                self.s.forward(9)
            else:
                self.s.pensize(1)
                self.s.forward(9)

        self.s.setheading(90)
        for i in range(1, 9):
            self.s.up()
            self.s.goto(i, 0)
            self.s.down()
            if i == 3 or i == 6:
                self.s.pensize(5)
                self.s.forward(9)
            else:
                self.s.pensize(1)
                self.s.forward(9)
        self.wn.update()
        self.wn.tracer(1)

    def writeCellSudoku(self, num, row, column):
        if (row, column) in self.sudokuDic.keys():
            self.sudokuDic[(row, column)].clear()
            self.sudokuDic[(row, column)].pensize()
            self.sudokuDic[(row, column)].write(f"{num}", font=("Calibri", 40, "normal"))
        else:
            cellT = turtle.Turtle()
            cellT.up()
            cellT.hideturtle()
            cellT.goto(column + .4, (9 - row) - 0.9)
            cellT.write(f"{num}", font=("Calibri", 40, "normal"))
            self.sudokuDic[(row, column)] = cellT

    def resetCellSudoku(self, row, column):
        if (row, column) in self.sudokuDic.keys():
            self.sudokuDic[(row, column)].clear()

