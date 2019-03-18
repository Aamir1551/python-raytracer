class Scene:
    def __init__(self, hittable, background_colour):
        self.hittable = hittable
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
        return closest_shape.color


