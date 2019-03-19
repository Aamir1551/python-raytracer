import ray
import numpy as np


CANVAS_HEIGHT = 500.0
CANVAS_WIDTH = 500.0

VIEWPOINT_HEIGHT = 1.0
VIEWPOINT_WIDTH = 1.0
VIEWPOINT_DIST = 0.5


class Canvas:

    @staticmethod
    def get_view_point(canvasx, canvasy):
        return [canvasx/CANVAS_WIDTH * VIEWPOINT_WIDTH - VIEWPOINT_WIDTH / 2,
                float(canvasy / CANVAS_HEIGHT * VIEWPOINT_HEIGHT * - VIEWPOINT_HEIGHT / 2), VIEWPOINT_DIST]

    @staticmethod
    def draw_canvas(scene, filename):
        f = open(filename, "w")
        f.write("P3 \n")
        f.write(str(int(CANVAS_WIDTH)) + " " + str(int(CANVAS_HEIGHT)) + "\n")
        f.write("255 \n")
        for i in range(0, int(CANVAS_HEIGHT)):
            for j in range(0, int(CANVAS_WIDTH)):
                [x, y, z] = Canvas.get_view_point(j, i)
                r = ray.Ray(np.array([0, 0, 0]), np.array([x, y, z]))
                f.write(Canvas.col_string(scene.trace_ray(r, 0.01)))
            f.write("\n")

    @staticmethod
    def col_string(color):
        return "{:03d}".format(int(color[0])) + " " "{:03d}".format(int(color[1])) + " " + "{:03d} ".format(int(color[2]))
