import math
import numpy as np
import tkinter as tk
import tkinter.font

WIDTH = HEIGHT = 600

root = tk.Tk()
canvas = tk.Canvas(root, width=WIDTH, height=WIDTH, bg="#222")
canvas.pack()
font_10 = tk.font.Font(family="Arial", size=10, weight="bold")


def hypotrochoid(value=None):
    canvas.delete("line")

    size = size_slider.get()
    r = r_slider.get() * size
    R = R_slider.get() * size
    d = d_slider.get() * size

    x_start = (R - r) * math.cos(0) + d * math.cos((R - r)/r * 0) + WIDTH / 2
    y_start = (R - r) * math.sin(0) - d * math.sin((R - r)/r * 0) + HEIGHT / 2
    for t in np.arange(0, 2 * math.pi * np.lcm(r, R) / R, 0.1):
        delta = R - r
        x = delta * math.cos(t) + d * math.cos(delta/r * t) + WIDTH / 2
        y = delta * math.sin(t) - d * math.sin(delta/r * t) + HEIGHT / 2
        canvas.create_line(x, y, x_start, y_start, fill="#ddd", width=1, tag="line")
        x_start = x
        y_start = y


if __name__ == "__main__":
    r_slider = tk.Scale(root, orient=tk.HORIZONTAL, from_=1, to=20, length=200, command=hypotrochoid,
                        resolution=1, label='r', bd=0, activebackground="#222", bg="#222", fg="#ddd",
                        troughcolor="#ddd", highlightbackground="#222", highlightcolor="#222",
                        font=font_10)
    R_slider = tk.Scale(root, orient=tk.HORIZONTAL, from_=1, to=20, length=200, command=hypotrochoid,
                        resolution=1, label='R', bd=0, activebackground="#222", bg="#222", fg="#ddd",
                        troughcolor="#ddd", highlightbackground="#222", highlightcolor="#222",
                        font=font_10)
    d_slider = tk.Scale(root, orient=tk.HORIZONTAL, from_=1, to=20, length=200, command=hypotrochoid,
                        resolution=1, label='d', bd=0, activebackground="#222", bg="#222", fg="#ddd",
                        troughcolor="#ddd", highlightbackground="#222", highlightcolor="#222",
                        font=font_10)
    size_slider = tk.Scale(root, orient=tk.VERTICAL, from_=5, to=15, length=100, command=hypotrochoid,
                           resolution=1, label='size', bd=0, activebackground="#222", bg="#222", fg="#ddd",
                           troughcolor="#ddd", highlightbackground="#222", highlightcolor="#222",
                           font=font_10)

    r_slider.place(x=20, y=530, width=130, bordermode=tk.OUTSIDE)
    R_slider.place(x=170, y=530, width=130, bordermode=tk.OUTSIDE)
    d_slider.place(x=320, y=530, width=130, bordermode=tk.OUTSIDE)
    size_slider.place(x=500, y=485, height=100, bordermode=tk.OUTSIDE)
    r_slider.set(2)
    hypotrochoid()

    root.mainloop()
