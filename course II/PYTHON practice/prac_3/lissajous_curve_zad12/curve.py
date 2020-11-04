from p5 import *


class Curve:

    def __init__(self):
        self.path = []
        self.current = Vector(0, 0)

    @property
    def x(self):
        return self.current.x

    @x.setter
    def x(self, value):
        self.current.x = value

    @property
    def y(self):
        return self.current.y

    @y.setter
    def y(self, value):
        self.current.y = value

    def add_point(self):
        self.path.append(self.current)

    def reset(self):
        self.path = []

    def show(self):
        stroke(255)
        stroke_weight(1)
        no_fill()
        begin_shape()

        vertex(self.path[0].x, self.path[0].y)
        for v in self.path:
            vertex(v.x, v.y)

        end_shape()

        stroke_weight(8)
        point(self.current.x, self.current.y)
        self.current = Vector(0, 0)
