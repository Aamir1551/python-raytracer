import numpy as np

class ray:
    def __init__(self, p, d):
        self.p = p
        self.d = d

class Sphere:

    def __init__(self, c, r, color):
        self.c = c
        self.r = r
        self.color = color

    def intersect(self, rayin):
        a = np.dot(rayin.d, rayin.d)
        b = 2 * np.dot(self.c , rayin.d)
        c = np.dot(self.c * -1, self.c * -1) - self.r * self.r

        dis = b*b - 4 * a * c
        if(dis >= 0):
            return self.color
        else:
            return False

class scene():
    def __init__(self, hittable):
        self.hittable = hittable


CANVAS_HEIGHT = 100.0
CANVAS_WIDTH = 200.0

VIEWPOINT_HEIGHT = 1.0
VIEWPOINT_WIDTH = 1.0
VIEWPOINT_DIST = 1.1

def getViewPointXYZ(canvasx, canvasy):
    return [ canvasx/ CANVAS_WIDTH * VIEWPOINT_WIDTH - VIEWPOINT_WIDTH /2,float(canvasy / CANVAS_HEIGHT * VIEWPOINT_HEIGHT * - VIEWPOINT_HEIGHT / 2), VIEWPOINT_DIST]

def drawcanvas(cscene, filename):
    f = open(filename, "w")
    f.write("P3 \n")
    f.write(str(int(CANVAS_WIDTH)) + " " + str(int(CANVAS_HEIGHT)) + "\n")
    f.write("255 \n")
    for i in range(0, int(CANVAS_HEIGHT)):
        for j in range(0, int(CANVAS_WIDTH)):
            [x, y, z] = getViewPointXYZ(j, i)
            r = ray(np.array([0,0,0]),np.array([x, y, z]))
            for o in cscene.hittable:
                color = o.intersect(r)
                if (color <> False):
                    f.write(color)
                else:
                    f.write("255   0   0 ")
        f.write("\n")



cscene  = scene([Sphere(np.array([0,-1, 3]), 0.9, "255 255   0 ")])
drawcanvas(cscene, "pic.ppm")




