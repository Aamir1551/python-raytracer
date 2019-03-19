import numpy as np


class Scene:
    def __init__(self, hittable, lights, background_colour):
        self.hittable = hittable
        self.lights = lights
        self.background_color = background_colour
    
    def get_closest_intersection(self, ray, t_min):
        closest_t = float("inf")
        closest_shape = None

        for shape in self.hittable:
            [t1, t2] = shape.intersect(ray)
            if t_min < t1 < closest_t:
                closest_t = t1
                closest_shape = shape
            if t_min < t2 < closest_t:
                closest_t = t2
                closest_shape = shape
        return closest_shape, closest_t

    def trace_ray(self, ray, t_min):
        
        closest_shape, closest_t = self.get_closest_intersection(ray, t_min)
        
        if closest_shape is None:
            return self.background_color

        point = ray.p + ray.d * closest_t
        normal = closest_shape.normal(point)
        return np.array(closest_shape.color) * self.compute_intensity(point, normal, closest_shape.specular, -ray.d, ray)

    def compute_intensity(self, point, normal, specular, viewpoint, ray):
        i = 0
        for light in self.lights:
            if light.type == "ambient":
                i += light.intensity
            else:
                
                shadow_sphere, shadow_t = self.get_closest_intersection(ray, 0.0001)
                if shadow_sphere != None:
                    continue
                
                
                if light.type == "point":
                    direction = light.props - point
                else:
                    direction = light.props
                    
                n_dot_l = np.dot(normal, direction)
                i += max(0, n_dot_l / np.sqrt(direction.dot(direction))) #did not divide by magnitude of n as its 1
                
                
                if(specular != -1):
                    r = 2 * normal * np.dot(normal, direction) - direction
                    r_dot_v = np.dot(r, viewpoint)
                    if(r_dot_v > 0):
                        i+= light.intensity * pow(r_dot_v/(np.dot(r, r) * np.dot(viewpoint, viewpoint) ** 0.5), specular)
        return min(i,1)

