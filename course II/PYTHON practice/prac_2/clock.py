from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import Color, Line
from kivy.uix.floatlayout import FloatLayout
from math import cos, sin, pi
from kivy.clock import Clock
from kivy.lang import Builder
import datetime

kv = '''
#:import math math

[ClockNumber@Label]:
    text: str(ctx.i)
    pos_hint: {"center_x": 0.5+0.42*math.sin(math.pi/6*(ctx.i-12)), "center_y": 0.5+0.42*math.cos(math.pi/6*(ctx.i-12))}
    font_size: self.height/16
    color: 0.83, 0.27, 0.68

<MyClockWidget>:
    face: face
    ticks: ticks
    FloatLayout:
        id: face
        size_hint: None, None
        pos_hint: {"center_x":0.5, "center_y":0.5}
        size: 0.9*min(root.size), 0.9*min(root.size)
        canvas:
            Color:
                rgb: 0.1, 0.1, 0.1
            Ellipse:
                size: self.size     
                pos: self.pos
        ClockNumber:
            i: 1
        ClockNumber:
            i: 2
        ClockNumber:
            i: 3
        ClockNumber:
            i: 4
        ClockNumber:
            i: 5
        ClockNumber:
            i: 6
        ClockNumber:
            i: 7
        ClockNumber:
            i: 8
        ClockNumber:
            i: 9
        ClockNumber:
            i: 10
        ClockNumber:
            i: 11
        ClockNumber:
            i: 12
    Ticks:
        id: ticks
        r: min(root.size)*0.9/2
'''
Builder.load_string(kv)


class MyClockWidget(FloatLayout):
    pass


class Ticks(Widget):
    def __init__(self, **kwargs):
        super(Ticks, self).__init__(**kwargs)
        self.bind(pos=self.update_clock)
        self.bind(size=self.update_clock)

    def update_clock(self, *args):
        self.canvas.clear()
        with self.canvas:
            time = datetime.datetime.now()
            Color(0.83, 0.68, 0.42)
            th = time.microsecond / 1000
            Line(points=[self.center_x,
                         self.center_y,
                         self.center_x + 0.8 * self.r * sin(2 * pi / 1000 * th),
                         self.center_y + 0.8 * self.r * cos(2 * pi / 1000 * th)],
                 width=1.2, cap="round")
            Color(0.68, 0.83, 0.27)
            th = time.second * 1000 + time.microsecond / 1000
            Line(points=[self.center_x,
                         self.center_y,
                         self.center_x + 0.7 * self.r * sin(2 * pi / (60 * 1000) * th),
                         self.center_y + 0.7 * self.r * cos(2 * pi / (60 * 1000) * th)],
                 width=2, cap="round")
            Color(0.42, 0.27, 0.83)
            th += time.minute * 60 * 1000
            Line(points=[self.center_x,
                         self.center_y,
                         self.center_x + 0.55 * self.r * sin(2 * pi / (60 * 60 * 1000) * th),
                         self.center_y + 0.55 * self.r * cos(2 * pi / (60 * 60 * 1000) * th)],
                 width=3, cap="round")
            Color(0.83, 0.42, 0.27)
            th += time.hour * 60 * 60 * 1000
            Line(points=[self.center_x,
                         self.center_y,
                         self.center_x + 0.4 * self.r * sin(2 * pi / (12 * 60 * 60 * 1000) * th),
                         self.center_y + 0.4 * self.r * cos(2 * pi / (12 * 60 * 60 * 1000) * th)],
                 width=4, cap="round")
            Label(text=(time.strftime('%H:%M:%S:%f %d.%m.%Y')[:12] +
                        time.strftime('%H:%M:%S:%f %d.%m.%Y')[15:]),
                  font_size=20, pos=(self.width - 180, 10))


class MyClockApp(App):
    def build(self):
        clock = MyClockWidget()
        Clock.schedule_interval(clock.ticks.update_clock, 0.001)
        return clock


if __name__ == '__main__':
    MyClockApp().run()
