from shapes import Triangle, Rectangle, Oval
import random

for i in range(10):
    r = Rectangle
    r.set_width(random.randint(10,100))
    r.set_height(random.randint(10,100))
    r.set_x(random.randint(-100,100))
    r.set_y(random.randint(-10,100))
    col = random.randint(1,4)
    if col == 1:
        r.set_color("Red")
    elif col == 2:
        r.set_color("Blue")
    elif col == 3:
        r.set_color("Green")
    else:
        r.set_color("Pink")
    r.draw()
