import math
import numpy as np
import tkinter as tk
import tkinter.font

WIDTH = HEIGHT = 600

root = tk.Tk()
canvas = tk.Canvas(root, width=WIDTH, height=WIDTH, bg="#222")
canvas.pack()
font_10 = tk.font.Font(family="Arial", size=10, weight="bold")


def roze(value=None):
    canvas.delete("line")

    n = n_slider.get()
    d = d_slider.get()
    size = size_slider.get()

    k = n / d
    x_start = WIDTH / 2 + size * math.cos(k * 0) * math.cos(0)
    y_start = HEIGHT / 2 + size * math.cos(k * 0) * math.sin(0)
    for t in np.arange(0, 40 * math.pi, 0.1):
        r = size * math.cos(k * t)
        x = r * math.cos(t) + WIDTH / 2
        y = r * math.sin(t) + HEIGHT / 2
        canvas.create_line(x, y, x_start, y_start, fill="#ddd", width=1, tag="line")
        x_start = x
        y_start = y


if __name__ == "__main__":
    n_slider = tk.Scale(root, orient=tk.HORIZONTAL, from_=1, to=7, length=200, command=roze,
                        resolution=0.5, label='n', bd=0, activebackground="#222", bg="#222", fg="#ddd",
                        troughcolor="#ddd", highlightbackground="#222", highlightcolor="#222",
                        font=font_10)
    d_slider = tk.Scale(root, orient=tk.HORIZONTAL, from_=1, to=9, length=200, command=roze,
                        resolution=0.5, label='d', bd=0, activebackground="#222", bg="#222", fg="#ddd",
                        troughcolor="#ddd", highlightbackground="#222", highlightcolor="#222",
                        font=font_10)
    size_slider = tk.Scale(root, orient=tk.VERTICAL, from_=100, to=300, length=100, command=roze,
                           resolution=25, label='size', bd=0, activebackground="#222", bg="#222", fg="#ddd",
                           troughcolor="#ddd", highlightbackground="#222", highlightcolor="#222",
                           font=font_10)
    n_slider.place(x=10, y=530, width=200, bordermode=tk.OUTSIDE)
    d_slider.place(x=270, y=530, width=200, bordermode=tk.OUTSIDE)
    size_slider.place(x=500, y=485, height=100, bordermode=tk.OUTSIDE)
    roze()

    root.mainloop()
