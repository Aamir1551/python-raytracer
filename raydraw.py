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
        b = 2 * np.dot(self.c, rayin.d)
        c = np.dot(self.c, self.c) - self.r * self.r

        dis = b*b - 4 * a * c
        if(dis >= 0):
            return self.color
        else:
            return False

class scene():
    def __init__(self, hittable):
        self.hittable = hittable


CANVAS_HEIGHT = 40
CANVAS_WIDTH = 50

VIEWPOINT_HEIGHT = 100
VIEWPOINT_WIDTH = 200
VIEWPOINT_DIST = 5

def getViewPointXYZ(canvasx, canvasy):
    return [canvasx/ CANVAS_WIDTH * VIEWPOINT_WIDTH - VIEWPOINT_WIDTH /2, canvasy / CANVAS_HEIGHT * VIEWPOINT_HEIGHT * - VIEWPOINT_HEIGHT / 2, VIEWPOINT_DIST]

def drawcanvas(cscene, filename):
    f = open(filename, "w")
    f.write("P3 \n")
    f.write(str(CANVAS_WIDTH) + " " + str(CANVAS_HEIGHT) + "\n")
    f.write("255 \n")
    for i in range(0, CANVAS_HEIGHT):
        for j in range(0, CANVAS_WIDTH):
            [x, y, z] = getViewPointXYZ(i, j)
            r = ray(np.array([0,0,0]),np.array([x, y, z]))
            for o in cscene.hittable:
                color = o.intersect(r)
                if (color <> False):
                    f.write(color)
                else:
                    f.write("255   0   0 ")
        f.write("\n")



cscene  = scene([Sphere(np.array([0,0,100]), 14, "255 255   0 ")])
drawcanvas(cscene, "pic.ppm")




