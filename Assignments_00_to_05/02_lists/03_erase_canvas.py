import tkinter as tk
import time

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400

CELL_SIZE = 40
ERASER_SIZE = 20

class EraseCanvas:
    def __init__(self, root):
        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
        self.canvas.pack()

        self.cells = []
        self.create_grid()

        self.eraser = None
        self.canvas.bind("<Button-1>", self.start_erasing)
        self.canvas.bind("<Motion>", self.erase)

    def create_grid(self):
        rows = CANVAS_HEIGHT // CELL_SIZE
        cols = CANVAS_WIDTH // CELL_SIZE
        for row in range(rows):
            for col in range(cols):
                x1 = col * CELL_SIZE
                y1 = row * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE
                rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="black")
                self.cells.append(rect)

    def start_erasing(self, event):
        x, y = event.x, event.y
        self.eraser = self.canvas.create_rectangle(
            x, y, x + ERASER_SIZE, y + ERASER_SIZE, fill="pink", outline=""
        )

    def erase(self, event):
        if self.eraser:
            x, y = event.x, event.y
            self.canvas.coords(
                self.eraser,
                x,
                y,
                x + ERASER_SIZE,
                y + ERASER_SIZE
            )

            overlapping = self.canvas.find_overlapping(x, y, x + ERASER_SIZE, y + ERASER_SIZE)
            for item in overlapping:
                if item != self.eraser:
                    self.canvas.itemconfig(item, fill="white")


def main():
    root = tk.Tk()
    root.title("Erase Canvas")
    app = EraseCanvas(root)
    root.mainloop()

if __name__ == "__main__":
    main()
