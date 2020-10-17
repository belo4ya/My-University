import math
import numpy as np
import tkinter as tk
import tkinter.font

WIDTH = HEIGHT = 600

root = tk.Tk()
canvas = tk.Canvas(root, width=WIDTH, height=WIDTH, bg="#222")
canvas.pack()
font_10 = tk.font.Font(family="Arial", size=10, weight="bold")


def lemniscate_line():
    x_start = (c * math.sqrt(2) * math.cos(0)) / (1 + math.sin(0) ** 2) + WIDTH / 2
    y_start = (c * math.sqrt(2) * math.sin(0) * math.cos(0)) / (1 + math.sin(0) ** 2) + HEIGHT / 2
    for t in np.arange(0, 2 * math.pi, 0.01):
        x = (c * math.sqrt(2) * math.cos(t)) / (1 + math.sin(t) ** 2) + WIDTH / 2
        y = (c * math.sqrt(2) * math.sin(t) * math.cos(t)) / (1 + math.sin(t) ** 2) + HEIGHT / 2
        canvas.create_line(x, y, x_start, y_start, fill="#ddd", width=1, tag="line")
        x_start = x
        y_start = y


def lemniscate_move(t):
    p = math.tan(math.pi / 4 - t) ** 1/2

    current_coords = canvas.coords(point)
    current_x = current_coords[0] + point_r / 2
    current_y = current_coords[1] + point_r / 2

    x = c * math.sqrt(2) * ((p + p**3) / (1 + p**4)) + WIDTH / 2 - current_x
    y = c * math.sqrt(2) * ((p - p**3) / (1 + p**4)) + HEIGHT / 2 - current_y

    canvas.move(point, x, y)
    root.after(1000 // 30, lemniscate_move, t + 0.01)


if __name__ == "__main__":
    c = HEIGHT / 3
    point_r = 15
    point = canvas.create_oval(((WIDTH - point_r) // 2, (HEIGHT - point_r) // 2),
                               ((WIDTH + point_r) // 2, (HEIGHT + point_r) // 2), fill="#ddd")

    lemniscate_line()
    lemniscate_move(0)

    root.mainloop()
