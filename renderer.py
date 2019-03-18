from sphere import *
from scene import *
from canvas import *

BACKGROUND_COLOUR = "255   0   0 "


hittables = [Sphere(np.array([0, -1, 3]), 0.9, "255 255   0 ")]

cscene = Scene(hittables, "0   0   0  ")

Canvas.draw_canvas(cscene, "pic.ppm")
