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
        if dis >= 0:
            return self.color
        else:
            return False