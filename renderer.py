from sphere import *
from scene import *
from canvas import *
from light import *

BACKGROUND_COLOUR = np.array([255, 255, 255])


hittables = [Sphere(np.array([1.3, 1, 3]), 1, [255, 0, 0], -1,  0.6),
             Sphere(np.array([3, 1, 5]), 1, [0, 0, 255], 500, 0.3),
             Sphere(np.array([5, 1, 4]), 1, [0, 255, 0], 500000000, 0.4),
             Sphere(np.array([0, -1000, 0]), 1000 ,[185,11,229], 10,1)]

lights = [Light("ambient", 0, -1), Light("point", 0.8, np.array([2, 1, 6])),
          Light("directional", 0.2, np.array([1, 4, 4])), 
          Light("point", 1, np.array([1.3, 1, 1]))]


cscene = Scene(hittables, lights, BACKGROUND_COLOUR)

Canvas.draw_canvas(cscene, "pic.ppm")

