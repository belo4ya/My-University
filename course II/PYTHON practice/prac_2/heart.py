import math
import tkinter as tk
import tkinter.font

WIDTH = HEIGHT = 600

root = tk.Tk()
canvas = tk.Canvas(root, width=WIDTH, height=WIDTH, bg="#222")
canvas.pack()
font_10 = tk.font.Font(family="Arial", size=10, weight="bold")


def get_horizontally_flip_matrix():
    return [
        [1, 0, 0],
        [0, -1, 0],
        [0, 0, 1]
    ]


def horizontally_flip(x, y):
    t_matrix = get_horizontally_flip_matrix()
    x = t_matrix[0][0] * x + t_matrix[1][0] * y + t_matrix[2][0]
    y = t_matrix[0][1] * x + t_matrix[1][1] * y + t_matrix[2][1]
    return x, y


def get_parametric_x(t, *args):
    return args[0] * (12 * math.sin(t) - 4 * math.sin(3 * t))


def get_parametric_y(t, *args):
    return args[0] * (13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t))


def animation(t, i, j):
    if t > 2 * math.pi:
        return

    x = get_parametric_x(t, a)
    y = get_parametric_y(t, a)

    # [Опционально] отражение по горизонтали и смещение к центру
    x, y = horizontally_flip(x, y)
    x += WIDTH / 2
    y += HEIGHT / 2

    coords.append(x)
    coords.append(y)

    # закрашивание фигуры
    canvas.create_polygon(coords)

    # отрисовка контура фигуры
    if len(coords) > 2:
        i += 2
        j += 2
        canvas.create_line(x, y, coords[i], coords[j], fill="#fff", width=2.5)

    root.after(1000 // 30, animation, t + 0.05, i, j)


if __name__ == "__main__":
    a = 10
    coords = []
    animation(0, -2, -1)

    root.mainloop()
