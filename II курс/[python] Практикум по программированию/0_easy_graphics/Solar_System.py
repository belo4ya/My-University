import tkinter as tk
from PIL import Image, ImageTk
import math

WIDTH = HEIGHT = 800

root = tk.Tk()
frame = tk.Canvas(root, width=WIDTH, height=WIDTH, bg="#2b1834")
frame.pack()


class Planet:

    def __init__(self, radius, orbit_radius, sprite, alpha=None, speed=None):
        self.radius = radius
        self.orbit_radius = orbit_radius
        self.alpha = alpha or 3 / 2 * math.pi
        self.speed = self.default_speed = speed or 1

        self._init_orbit()
        self.sprite = self._init_sprite(sprite)
        self.canvas_obj = frame.create_image(WIDTH // 2, (HEIGHT - self.orbit_radius) // 2, image=self.sprite)

    def __str__(self):
        return f"<Planet> (radius={self.radius}, orbital_radius={self.orbit_radius})"

    __repr__ = __str__

    def _init_orbit(self):
        frame.create_oval(((WIDTH - self.orbit_radius) // 2, (HEIGHT - self.orbit_radius) // 2),
                          ((WIDTH + self.orbit_radius) // 2, (HEIGHT + self.orbit_radius) // 2))

    def _init_sprite(self, sprite):
        sprite = Image.open(sprite).resize((int(self.radius), int(self.radius)), Image.ANTIALIAS)
        sprite = ImageTk.PhotoImage(sprite)
        return sprite

    def rotate_move(self):
        self.alpha -= 0.015 * self.speed

        planet_x, planet_y = frame.coords(self.canvas_obj)
        planet_x = WIDTH / 2 + self.orbit_radius / 2 * math.cos(self.alpha) - planet_x
        planet_y = HEIGHT / 2 + self.orbit_radius / 2 * math.sin(self.alpha) - planet_y

        frame.move(self.canvas_obj, planet_x, planet_y)
        root.after(1000 // 30, self.rotate_move)

    def change_speed(self, value):
        self.speed = self.default_speed if abs(self.speed + value) > 20 else self.speed + value


def speed_up(event):
    for planet in planets:
        planet.change_speed(+0.2)


def speed_down(event):
    for planet in planets:
        planet.change_speed(-0.2)


if __name__ == '__main__':
    SUN_R = 150
    EARTH_R = SUN_R // (109 // 10)  # Радиус Солнца в 109 раз больше радиуса Земли (=6371)

    MERCURY_ORBIT_R = SUN_R + 40
    MERCURY_R = EARTH_R // 2.6  # Радиус = 2439

    VENUS_ORBIT_R = MERCURY_ORBIT_R + 35
    VENUS_R = EARTH_R // 1.1  # Радиус Меркурия = 6050

    EARTH_ORBIT_R = VENUS_ORBIT_R + 45

    MARS_ORBIT_R = EARTH_ORBIT_R + 50
    MARS_R = EARTH_R // 1.9  # Радиус Марса = 3389

    JUPITER_ORBIT_R = MARS_ORBIT_R + 105
    JUPITER_R = EARTH_R // (0.1 * 2)  # Радиус Юпитера = 69911

    SATURN_ORBIT_R = JUPITER_ORBIT_R + 140
    SATURN_R = EARTH_R // (0.12 * 2)  # Радиус Сатурна = 58232

    URANUS_ORBIT_R = SATURN_ORBIT_R + 110
    URANUS_R = EARTH_R // (0.25 * 2)  # Радиус Урана = 25362

    NEPTUNE_ORBIT_R = URANUS_ORBIT_R + 75
    NEPTUNE_R = EARTH_R // (0.26 * 2)  # Радиус Нептуна = 24622

    # создание Солнца
    sun_sprite = Image.open("images/Sun.png").resize((SUN_R, SUN_R), Image.ANTIALIAS)
    sun_sprite = ImageTk.PhotoImage(sun_sprite)
    sun = frame.create_image(WIDTH // 2, HEIGHT // 2, image=sun_sprite)

    # создание Планет
    planets = [
        Planet(MERCURY_R, MERCURY_ORBIT_R, "images/mercury.png", alpha=1, speed=1.1),
        Planet(VENUS_R, VENUS_ORBIT_R, "images/venus.png", alpha=2, speed=0.95),
        Planet(EARTH_R, EARTH_ORBIT_R, "images/earth.png", alpha=3, speed=1),
        Planet(MARS_R, MARS_ORBIT_R, "images/mars.png", alpha=4, speed=0.85),
        Planet(JUPITER_R, JUPITER_ORBIT_R, "images/jupiter.png", alpha=5, speed=0.09),
        Planet(SATURN_R, SATURN_ORBIT_R, "images/saturn.png", alpha=6, speed=0.08),
        Planet(URANUS_R, URANUS_ORBIT_R, "images/uranus.png", alpha=7, speed=0.055),
        Planet(NEPTUNE_R, NEPTUNE_ORBIT_R, "images/neptune.png", alpha=8, speed=0.015)
    ]

    for i in planets:
        i.rotate_move()

    frame.bind('<Left>', speed_down)
    frame.bind('<Right>', speed_up)
    frame.focus_set()

    root.mainloop()
