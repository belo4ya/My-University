import math
import numpy as np
import tkinter as tk
import tkinter.font

WIDTH = HEIGHT = 600

root = tk.Tk()
canvas = tk.Canvas(root, width=WIDTH, height=WIDTH, bg="#222")
canvas.pack()
font_10 = tk.font.Font(family="Arial", size=10, weight="bold")


def sgn(w):
    if w < 0:
        return -1
    elif w > 0:
        return 1
    return 0


def superellipse(value=None):
    canvas.delete("line")

    a = a_slider.get()
    b = b_slider.get()
    n = n_slider.get()
    size = size_slider.get()

    x_start = WIDTH / 2 + size * abs(math.cos(0)) ** (2 / n) * a * sgn(math.cos(0))
    y_start = HEIGHT / 2 + size * abs(math.sin(0)) ** (2 / n) * b * sgn(math.sin(0))
    for t in np.arange(0, 2 * math.pi + 0.1, 0.1):
        x = WIDTH / 2 + size * abs(math.cos(t)) ** (2 / n) * a * sgn(math.cos(t))
        y = HEIGHT / 2 + size * abs(math.sin(t)) ** (2 / n) * b * sgn(math.sin(t))
        canvas.create_line(x, y, x_start, y_start, fill="#ddd", width=1, tag="line")
        x_start = x
        y_start = y


if __name__ == "__main__":
    n_slider = tk.Scale(root, orient=tk.HORIZONTAL, from_=0.1, to=10, length=200, command=superellipse,
                        resolution=0.1, label='n', bd=0, activebackground="#222", bg="#222", fg="#ddd",
                        troughcolor="#ddd", highlightbackground="#222", highlightcolor="#222",
                        font=font_10)
    a_slider = tk.Scale(root, orient=tk.HORIZONTAL, from_=0.5, to=3, length=200, command=superellipse,
                        resolution=0.5, label='a', bd=0, activebackground="#222", bg="#222", fg="#ddd",
                        troughcolor="#ddd", highlightbackground="#222", highlightcolor="#222",
                        font=font_10)
    b_slider = tk.Scale(root, orient=tk.HORIZONTAL, from_=0.5, to=3, length=200, command=superellipse,
                        resolution=0.5, label='b', bd=0, activebackground="#222", bg="#222", fg="#ddd",
                        troughcolor="#ddd", highlightbackground="#222", highlightcolor="#222",
                        font=font_10)
    size_slider = tk.Scale(root, orient=tk.VERTICAL, from_=100, to=300, length=100, command=superellipse,
                           resolution=25, label='size', bd=0, activebackground="#222", bg="#222", fg="#ddd",
                           troughcolor="#ddd", highlightbackground="#222", highlightcolor="#222",
                           font=font_10)
    n_slider.place(x=10, y=530, width=140, bordermode=tk.OUTSIDE)
    a_slider.place(x=160, y=530, width=140, bordermode=tk.OUTSIDE)
    b_slider.place(x=310, y=530, width=140, bordermode=tk.OUTSIDE)
    size_slider.place(x=500, y=485, height=100, bordermode=tk.OUTSIDE)

    superellipse()

    root.mainloop()
