from sphere import *
from scene import *
from canvas import *

CANVAS_HEIGHT = 100.0
CANVAS_WIDTH = 200.0

VIEWPOINT_HEIGHT = 1.0
VIEWPOINT_WIDTH = 1.0
VIEWPOINT_DIST = 1.1

BACKGROUND_COLOUR = "255   0   0 "


hittables = [Sphere(np.array([0, -1, 3]), 0.9, "255 255   0 ")]

cscene = Scene(hittables)

Canvas.draw_canvas(cscene, "pic.ppm")
