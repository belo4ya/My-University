from p5 import *
from curve import Curve

WIDTH = 600
HEIGHT = 600

angle = 0
w = 120
cols = WIDTH // w - 1
rows = HEIGHT // w - 1
curves = []


def setup():
    size(HEIGHT, WIDTH)

    for j in range(rows):
        curves.append(list())
        for i in range(cols):
            curves[j].append(Curve())


def draw():
    global angle

    background(51)
    d = w - 0.2 * w
    r = d / 2

    no_fill()
    stroke(255)
    for i in range(cols):
        cx = w + i * w + w / 2
        cy = w / 2
        stroke_weight(1)
        stroke(255)
        ellipse(cx, cy, d, d)
        x = r * cos(angle * (i + 1) - HALF_PI)
        y = r * sin(angle * (i + 1) - HALF_PI)
        stroke_weight(8)
        stroke(255)
        point(cx + x, cy + y)
        stroke(255, 150)
        stroke_weight(1)
        line(cx + x, 0, cx + x, height)

        for j in range(rows):
            curves[j][i].x = cx + x

    no_fill()
    stroke(255)
    for j in range(rows):
        cx = w / 2
        cy = w + j * w + w / 2
        stroke_weight(1)
        stroke(255)
        ellipse(cx, cy, d, d)
        x = r * cos(angle * (j + 1) - HALF_PI)
        y = r * sin(angle * (j + 1) - HALF_PI)
        stroke_weight(8)
        stroke(255)
        point(cx + x, cy + y)
        stroke(255, 150)
        stroke_weight(1)
        line(0, cy + y, width, cy + y)

        for i in range(cols):
            curves[j][i].y = cy + y

    for j in range(rows):
        for i in range(cols):
            curves[j][i].add_point()
            curves[j][i].show()

    if (angle := angle - 0.05) < - TWO_PI:
        for j in range(rows):
            for i in range(cols):
                curves[j][i].reset()

        angle = 0
        clear()


if __name__ == '__main__':
    run()
