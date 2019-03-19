import ray
import numpy as np


CANVAS_HEIGHT = 200
CANVAS_WIDTH = 200

VIEWPOINT_HEIGHT = 1.5
VIEWPOINT_WIDTH = 1.5
VIEWPOINT_DIST = 1
RECURSION_DEPTH = 2

EYE_LOCATION = np.array([VIEWPOINT_WIDTH / 2, 0, 0])

class Canvas:

    @staticmethod
    def get_view_point(canvasx, canvasy):
        return [float(canvasx) / CANVAS_WIDTH * VIEWPOINT_WIDTH, float(canvasy) / CANVAS_HEIGHT * VIEWPOINT_HEIGHT,
                 VIEWPOINT_DIST]

    @staticmethod
    def draw_canvas(scene, filename):
        f = open(filename, "w")
        f.write("P3 \n")
        f.write(str(int(CANVAS_WIDTH)) + " " + str(int(CANVAS_HEIGHT)) + "\n")
        f.write("255 \n")
        for i in range(0, int(CANVAS_HEIGHT)):
            for j in range(0, int(CANVAS_WIDTH)):
                [x, y, z] = Canvas.get_view_point(j, i)
                r = ray.Ray(EYE_LOCATION, np.array([x, y, z]))
                f.write(Canvas.col_string(scene.trace_ray(r, 0, RECURSION_DEPTH)))
            f.write("\n")

    @staticmethod
    def col_string(color):
        return "{:03d}".format(int(color[0])) + " " + "{:03d}".format(int(color[1])) + " " \
               + "{:03d} ".format(int(color[2]))

