import numpy as np
import tkinter as tk
import tkinter.font

from scipy.integrate import odeint

WIDTH = HEIGHT = 600

root = tk.Tk()
canvas = tk.Canvas(root, width=WIDTH, height=WIDTH, bg="#222")
canvas.pack()

font_10 = tk.font.Font(family="Arial", size=10, weight="bold")
colors = [
    "#e570a9", "#df72b1", "#d975b9", "#d278c0", "#ca7bc7",
    "#c17fcd", "#b782d3", "#ad86d8", "#a289db", "#978cdf",
    "#8b8fe1", "#7f92e2", "#7295e3", "#6497e3", "#5699e2",
    "#479ce0", "#379dde", "#259fdb", "#07a0d7", "#00a2d3",
    "#00a3ce", "#00a3c9", "#00a4c4", "#00a4be", "#00a5b8",
    "#00a5b2", "#05a5ab", "#1ea5a5", "#2ca49f", "#38a499"
]
after_id = None


def equation(state, t):
    global sigma
    global rho

    x, y, z = state
    x_ = sigma * (y - x)
    y_ = x * (rho - z) - y
    z_ = x * y - beta * z
    return x_, y_, z_


def animation(i):
    global after_id

    if i >= len(states):
        return

    # Наивное 3d преобразование (x = x / z, y = y / z)
    canvas.create_line((states[i][0] / states[i][2]) * 70 + 300, (states[i][1] / states[i][2]) * 70 + 100,
                       (states[i - 1][0] / states[i - 1][2]) * 70 + 300, (states[i - 1][1] / states[i - 1][2]) * 70 + 100,
                       tag="line")

    # y, z
    canvas.create_line(states[i][1] * size + 100, states[i][2] * size + 320,
                       states[i - 1][1] * size + 100, states[i - 1][2] * size + 320, tag="line")

    # x, y
    canvas.create_line(states[i][0] * size + 300, states[i][1] * size + 400,
                       states[i - 1][0] * size + 300, states[i - 1][1] * size + 400, tag="line")

    # x, z
    canvas.create_line(states[i][0] * size + 500, states[i][2] * size + 320,
                       states[i - 1][0] * size + 500, states[i - 1][2] * size + 320, tag="line")

    canvas.itemconfigure("line", fill=colors[i % len(colors)])

    after_id = root.after(10, animation, i + 1)


def update_data(value):
    global sigma
    global rho
    global states
    global after_id

    sigma = sigma_slider.get()
    rho = rho_slider.get()

    states = odeint(equation, state_0, t)

    canvas.delete("line")

    if after_id:
        root.after_cancel(after_id)
        after_id = None

    animation(1)


if __name__ == '__main__':
    sigma = 10
    rho = 28
    beta = 8 / 3
    state_0 = (4, 2, 4)  # координаты начальной точки

    t = np.arange(0, 40, 0.025)
    size = 3

    states = odeint(equation, state_0, t)

    sigma_slider = tk.Scale(root, orient=tk.HORIZONTAL, from_=3, to=15, length=200, command=update_data,
                            resolution=1, label='sigma', bd=0, activebackground="#222", bg="#222", fg="#ddd",
                            troughcolor="#ddd", highlightbackground="#222", highlightcolor="#222",
                            font=font_10)
    rho_slider = tk.Scale(root, orient=tk.HORIZONTAL, from_=4, to=40, length=200, command=update_data,
                          resolution=2, label='rho', bd=0, activebackground="#222", bg="#222", fg="#ddd",
                          troughcolor="#ddd", highlightbackground="#222", highlightcolor="#222",
                          font=font_10)

    y_z = tk.Label(text="y, z", font=font_10)
    x_y = tk.Label(text="x, y", font=font_10)
    x_z = tk.Label(text="x, z", font=font_10)
    d3 = tk.Label(text="3D", font=font_10)

    sigma_slider.place(x=200 / 3, y=530, width=200, bordermode=tk.OUTSIDE)
    rho_slider.place(x=200 / 3 * 2 + 200, y=530, width=200, bordermode=tk.OUTSIDE)
    sigma_slider.set(10)
    rho_slider.set(28)

    y_z.place(x=100, y=490)
    x_y.place(x=300, y=490)
    x_z.place(x=500, y=490)
    d3.place(x=180, y=50)

    animation(1)
    root.mainloop()
