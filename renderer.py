from sphere import *
from scene import *
from canvas import *
from light import *

BACKGROUND_COLOUR = [255, 0, 0]


hittables = [Sphere(np.array([0, -1, 3]), 1, [255, 0, 0]),
             Sphere(np.array([2, 0, 4]), 1, [0, 0, 255]),
             Sphere(np.array([0, -5001, 0]), 5000, [0, 255, 0])]

lights = [Light("ambient", 0.2, -1), Light("point", 0.6, np.array([2, 1, 6])),
          Light("directional", 0.2, np.array([1, 4, 4]))]


cscene = Scene(hittables, lights, BACKGROUND_COLOUR)

Canvas.draw_canvas(cscene, "pic.ppm")
