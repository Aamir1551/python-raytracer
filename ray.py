import numpy as np


class Ray:
    def __init__(self, p, d):
        self.p = p
        self.d = d / np.sqrt(np.sum(d**2))

    @staticmethod
    def reflect_ray(n, d):
        return 2 * n * np.dot(n, d) - d
