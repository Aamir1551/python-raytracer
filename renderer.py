from sphere import *
from scene import *
from canvas import *

BACKGROUND_COLOUR = "255   0   0 "


hittables = [Sphere(np.array([0, -1, 3]), 1, "255 255   0 "),
             Sphere(np.array([2, 0, 4]), 1, "0   0   255 ")]

cscene = Scene(hittables, "0   0   0  ")

Canvas.draw_canvas(cscene, "pic.ppm")
