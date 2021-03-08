import math
import numpy as np
import tkinter as tk
import tkinter.font

WIDTH = HEIGHT = 600

root = tk.Tk()
canvas = tk.Canvas(root, width=WIDTH, height=WIDTH, bg="#222")
canvas.pack()
font_10 = tk.font.Font(family="Arial", size=10, weight="bold")


class Star:
    k = 1
    n = 5
    m = 3

    def __init__(self, center: tuple, r: float):
        self.center = center
        self.r = r

        self._t = np.arange(0, 2 * math.pi + 0.01, 0.01)
        self._p = (np.cos((2 * np.arcsin(self.k) + np.pi * self.m) / (2 * self.n)) /
                   np.cos((2 * np.arcsin(self.k * np.cos(self.n * self._t)) + np.pi * self.m) / (2 * self.n)))

        self.cartesian_coords = []
        for i in range(len(self._t)):
            self.cartesian_coords.append([
                r * self.x_to_cartesian(self._p[i], self._t[i]) + self.center[0],
                r * self.y_to_cartesian(self._p[i], self._t[i]) + self.center[1]
            ])

    @staticmethod
    def x_to_cartesian(r, theta):
        return r * math.cos(theta)

    @staticmethod
    def y_to_cartesian(r, theta):
        return r * math.sin(theta)

    @staticmethod
    def _rotate(point: tuple, pivot: tuple, angle: float):
        x_0, y_0 = pivot
        x, y = point
        return x_0 + (x - x_0) * math.cos(angle) - (y - y_0) * math.sin(angle),\
               y_0 + (y - y_0) * math.cos(angle) + (x - x_0) * math.sin(angle)

    def get_center(self):
        return self.center

    def rotate(self, pivot: tuple, angle: float):
        for i in range(len(self.cartesian_coords)):
            self.cartesian_coords[i] = [
                self._rotate((self.cartesian_coords[i][0], self.cartesian_coords[i][1]), pivot, angle)[0],
                self._rotate((self.cartesian_coords[i][0], self.cartesian_coords[i][1]), pivot, angle)[1]
            ]

    def move(self, x, y):
        for i in range(len(self.cartesian_coords)):
            self.cartesian_coords[i] = [
                self.cartesian_coords[i][0] + x,
                self.cartesian_coords[i][1] + y
            ]

        self.center = (self.center[0] + x, self.center[1] + y)

    def draw(self):
        for i in range(1, len(self.cartesian_coords)):
            canvas.create_line(self.cartesian_coords[i][0], self.cartesian_coords[i][1],
                               self.cartesian_coords[i-1][0], self.cartesian_coords[i-1][1], fill="#fff", tag="line")


def get_x(r, theta):
    return r * math.cos(theta)


def get_y(r, theta):
    return r * math.sin(theta)


def animation(alpha):
    canvas.delete("line")
    alpha += 0.015 * speed
    beta = 15 * speed if abs(15 * speed) < 46 else 45 * np.sign(speed)

    center_x, center_y = star.get_center()

    star_x = WIDTH / 2 + r / 2 * math.cos(alpha) - center_x
    star_y = HEIGHT / 2 + r / 2 * math.sin(alpha) - center_y

    star.rotate(star.get_center(), beta)
    star.move(star_x, star_y)
    star.draw()

    root.after(1000 // 30, animation, alpha)


def left_speed(e):
    global speed
    speed += 0.25 if speed < 4 else 0


def right_speed(e):
    global speed
    speed += -0.25 if speed > -4 else 0


if __name__ == '__main__':
    r = 300
    canvas.create_oval(((WIDTH - r) / 2, (HEIGHT - r) / 2),
                       ((WIDTH + r) / 2, (HEIGHT + r) / 2), outline="#84c3be")

    star = Star((0, 0), 20)
    speed = 2

    canvas.bind('<Left>', left_speed)
    canvas.bind('<Right>', right_speed)
    canvas.focus_set()

    animation(0)
    root.mainloop()
