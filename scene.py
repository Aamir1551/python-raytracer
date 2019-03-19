import numpy as np


class Scene:
    def __init__(self, hittable, lights, background_colour):
        self.hittable = hittable
        self.lights = lights
        self.background_color = background_colour

    def trace_ray(self, ray, t_min):
        closest_t = float("inf")
        closest_shape = None

        for shape in self.hittable:
            [t1, t2] = shape.intersect(ray)
            if t_min < t1 < closest_t:
                closest_t = t1
                closest_shape = shape
            if t_min < t2 < t1 < closest_t:
                closest_t = t2
                closest_shape = shape
        if closest_shape is None:
            return self.background_color

        point = ray.p
        normal = closest_shape.normal(point)
        return np.array(closest_shape.color) * self.compute_intensity(point, normal)

    def compute_intensity(self, point, normal):
        i = 0
        for light in self.lights:
            if light.type == "ambient":
                i += light.intensity
            else:
                if light.type == "point":
                    direction = light.props - point
                else:
                    direction = light.props
                n_dot_l = np.dot(normal, direction)
                i += max(0, n_dot_l / np.sqrt(direction.dot(direction))) #did not divide by magnitude of n as its 1
        return i

