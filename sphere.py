import numpy as np


class Sphere:

    def __init__(self, c, r, color, specular):
        self.c = c
        self.r = r
        self.color = color
        self.specular = specular

    def intersect(self, rayin):

        oc = rayin.p - self.c

        a = np.dot(rayin.d, rayin.d)
        b = 2 * np.dot(oc, rayin.d)
        c = np.dot(oc, oc) - self.r ** 2

        dis = (b**2 - 4 * a * c)

        if dis < 0:
            return float("inf"), float("inf")
        else:
            return [(-b + np.sqrt(dis)) / (2*a), (-b - np.sqrt(dis))/(2*a)]

    def normal(self, point):
        normal = point - self.c
        return normal / np.dot(normal, normal) ** 0.5



