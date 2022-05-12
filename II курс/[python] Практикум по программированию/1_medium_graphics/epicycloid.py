import math
import numpy as np
import tkinter as tk
import tkinter.font

WIDTH = HEIGHT = 600

root = tk.Tk()
canvas = tk.Canvas(root, width=WIDTH, height=WIDTH, bg="#222")
canvas.pack()
font_10 = tk.font.Font(family="Arial", size=10, weight="bold")


def epicycloid(value=None):
    canvas.delete("line")

    r = r_slider.get()
    k = k_slider.get()
    R = k * r

    x_start = (R + r) * math.cos(0) - r * math.cos((R + r)/r * 0) + WIDTH / 2
    y_start = (R + r) * math.sin(0) - r * math.sin((R + r)/r * 0) + HEIGHT / 2
    for t in np.arange(0, 100, 0.1):
        delta = R + r
        x = delta * math.cos(t) - r * math.cos(delta/r * t) + WIDTH / 2
        y = delta * math.sin(t) - r * math.sin(delta/r * t) + HEIGHT / 2
        canvas.create_line(x, y, x_start, y_start, fill="#ddd", width=1, tag="line")
        x_start = x
        y_start = y


if __name__ == "__main__":
    r_slider = tk.Scale(root, orient=tk.HORIZONTAL, from_=15, to=30, length=100, command=epicycloid,
                        resolution=1, label='r', bd=0, activebackground="#222", bg="#222", fg="#ddd",
                        troughcolor="#ddd", highlightbackground="#222", highlightcolor="#222",
                        font=font_10)
    k_slider = tk.Scale(root, orient=tk.HORIZONTAL, from_=1, to=9, length=100, command=epicycloid,
                        resolution=0.2, label='k', bd=0, activebackground="#222", bg="#222", fg="#ddd",
                        troughcolor="#ddd", highlightbackground="#222", highlightcolor="#222",
                        font=font_10)

    r_slider.place(x=20, y=530, width=200, bordermode=tk.OUTSIDE)
    k_slider.place(x=240, y=530, width=200, bordermode=tk.OUTSIDE)
    r_slider.set(20)
    epicycloid()

    root.mainloop()
