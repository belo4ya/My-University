from tkinter import *
import math

WIDTH = 600
HEIGHT = 600
center_x = WIDTH / 2
center_y = HEIGHT / 2
R = 200
r = 20
ugol = 0
ugol_sin = 0
shag = 0.1
shag_sin = 5
speed = 1

root = Tk()
c = Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
c.pack()

big_ball = c.create_oval(center_x - R, center_y - R, center_x + R, center_y + R, fill='green')
small_ball = c.create_oval(center_x - r - R, center_y - r, center_x + r - R, center_y + r, fill='red')


def get_middle(x1, x2):
    return abs(x1+x2)/2


def motion(): 
    global ugol, ugol_sin, way, speed
    if ugol >= 360:
        ugol = 0
    if ugol_sin >= 360:
        ugol_sin = 0
        
    x1 = center_x -(math.sin(math.radians(ugol)) * R * (math.cos(math.radians(ugol_sin)) + 5)/(5)) - r
    x2 = center_x -(math.sin(math.radians(ugol)) * R * (math.cos(math.radians(ugol_sin)) + 5)/(5)) + r
    y2 = center_y +(math.cos(math.radians(ugol)) * R * (math.cos(math.radians(ugol_sin)) + 5)/(5)) + r
    y1 = center_y +(math.cos(math.radians(ugol)) * R * (math.cos(math.radians(ugol_sin)) + 5)/(5)) - r

    c.coords(small_ball, x1, y1, x2, y2)
    x_cen = get_middle(x1, x2)
    y_cen = get_middle(y1, y2)
    c.create_oval(x_cen-1, y_cen-1, x_cen+1, y_cen+1, fill = "blue", outline = "blue")
    ugol += shag
    ugol_sin += shag_sin
    root.after(speed, motion)


motion() 
root.mainloop()
