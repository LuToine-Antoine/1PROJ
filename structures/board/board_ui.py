import tkinter as tk


class UIBoard:

    def __init__(self):
        self._root = tk.Tk()
        self._root.title("Yinch by LLT")
        self._canvas = tk.Canvas(self._root, height=700, width=700)

        self.draw_triangles()

        self._canvas.pack()
        self._root.mainloop()

    def draw_triangles(self):
        """
        Draw the board in a window.
        :return: nothing
        """
        x1, y1 = 225, 25
        x2, y2 = 200, 75
        x3, y3 = 250, 75
        x4, y4 = 250, 75
        x5, y5 = 225, 25
        x6, y6 = 275, 25
        for i in range(10):
            if i == 0:
                for j in range(4):
                    self._canvas.create_polygon(x1 + 50 * j, y1, x2 + 50 * j, y2, x3 + 50 * j, y3, fill="",
                                                outline="black")
                for j in range(3):
                    self._canvas.create_polygon(x4 + 50 * j, y4, x5 + 50 * j, y5, x6 + 50 * j, y6, fill="",
                                                outline="black")
            if 0 < i < 4:
                for j in range(11 + i * 2):
                    if j % 2 == 0:
                        self._canvas.create_polygon(x1 - 25 * (2 + i) + 25 * j, y1 + 50 * i, x2 - 25 * (2 + i) + 25 * j,
                                                    y2 + 50 * i, x3 - 25 * (2 + i) + 25 * j, y3 + 50 * i, fill="",
                                                    outline="black")
                    else:
                        self._canvas.create_polygon(x4 - 25 * (1 + i) + 25 * (j - 2), y4 + 50 * i,
                                                    x5 - 25 * (1 + i) + 25 * (j - 2), y5 + 50 * i,
                                                    x6 - 25 * (1 + i) + 25 * (j - 2), y6 + 50 * i, fill="",
                                                    outline="black")
            if i == 6:
                for j in range(9):
                    self._canvas.create_polygon(x1 - 125 + 50 * j, y1 + 250, x2 - 125 + 50 * j, y2 + 250,
                                                x3 - 125 + 50 * j,
                                                y3 + 250, fill="", outline="black")
                for j in range(8):
                    self._canvas.create_polygon(x4 - 125 + 50 * j, y4 + 250, x5 - 125 + 50 * j, y5 + 250,
                                                x6 - 125 + 50 * j,
                                                y6 + 250, fill="", outline="black")
            if i == 5:
                for j in range(9):
                    self._canvas.create_polygon(x4 - 150 + 50 * j, y4 + 200, x5 - 150 + 50 * j, y5 + 200,
                                                x6 - 150 + 50 * j,
                                                y6 + 200, fill="", outline="black")
                for j in range(8):
                    self._canvas.create_polygon(x1 - 100 + 50 * j, y1 + 200, x2 - 100 + 50 * j, y2 + 200,
                                                x3 - 100 + 50 * j,
                                                y3 + 200, fill="", outline="black")
            if 9 > i > 5:
                for j in range(11 + (i - 5) * 2):
                    if j % 2 == 0:
                        self._canvas.create_polygon(x4 - 25 * (1 + i - 5) + 25 * (j - 2), y4 + 700 - 50 * i,
                                                    x5 - 25 * (1 + i - 5) + 25 * (j - 2), y5 + 700 - 50 * i,
                                                    x6 - 25 * (1 + i - 5) + 25 * (j - 2), y6 + 700 - 50 * i, fill="",
                                                    outline="black")
                    else:
                        self._canvas.create_polygon(x1 - 25 * (2 + i - 5) + 25 * j, y1 + 700 - 50 * i,
                                                    x2 - 25 * (2 + i - 5) + 25 * j, y2 + 700 - 50 * i,
                                                    x3 - 25 * (2 + i - 5) + 25 * j, y3 + 700 - 50 * i, fill="",
                                                    outline="black")
            if i == 9:
                for j in range(4):
                    self._canvas.create_polygon(x4 - 25 + 50 * j, y4 + 450, x5 - 25 + 50 * j, y5 + 450,
                                                x6 - 25 + 50 * j,
                                                y6 + 450, fill="", outline="black")
                for j in range(3):
                    self._canvas.create_polygon(x1 + 25 + 50 * j, y1 + 450, x2 + 25 + 50 * j, y2 + 450,
                                                x3 + 25 + 50 * j,
                                                y3 + 450, fill="", outline="black")

board = UIBoard()
