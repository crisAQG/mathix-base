from mathix.random import random
from mathix.trigonometry import *


class noise2:
    def __init__(self, scale=70.0, octaves=3, persistence=0.5, lacunarity=2.0, amplitude=1.0, seed=None):
        self.scale = scale
        self.octaves = octaves
        self.persistence = persistence
        self.lacunarity = lacunarity
        self.amplitude = amplitude
        self.seed = seed
        self.gradients = {}
        if seed is not None:
            random().randint(0, 10000)

    def _generate_gradient(self, ix, iy):
        angle = random().uniform(0, 2 * 3.141592653589793)
        return cos(angle), sin(angle)

    def _get_gradient(self, ix, iy):
        key = (ix, iy)
        if key not in self.gradients:
            self.gradients[key] = self._generate_gradient(ix, iy)
        return self.gradients[key]

    def _dot_grid_gradient(self, ix, iy, x, y):
        gradient = self._get_gradient(ix, iy)
        dx = x - ix
        dy = y - iy
        return dx * gradient[0] + dy * gradient[1]

    def _fade(self, t):
        return 6 * t**5 - 15 * t**4 + 10 * t**3

    def _lerp(self, a, b, t):
        return a + t * (b - a)

    def _perlin(self, x, y):
        x0 = int(floor(x))
        x1 = x0 + 1
        y0 = int(floor(y))
        y1 = y0 + 1

        sx = self._fade(x - x0)
        sy = self._fade(y - y0)

        n0 = self._dot_grid_gradient(x0, y0, x, y)
        n1 = self._dot_grid_gradient(x1, y0, x, y)
        ix0 = self._lerp(n0, n1, sx)

        n0 = self._dot_grid_gradient(x0, y1, x, y)
        n1 = self._dot_grid_gradient(x1, y1, x, y)
        ix1 = self._lerp(n0, n1, sx)

        return self._lerp(ix0, ix1, sy)

    def get(self, x, y):
        """Devuelve el valor de ruido normalizado entre 0 y 1, escalado por 'amplitude'"""
        total = 0.0
        max_value = 0.0
        frequency = 1.0
        amplitude = 1.0

        for _ in range(self.octaves):
            nx = x / self.scale * frequency
            ny = y / self.scale * frequency
            total += self._perlin(nx, ny) * amplitude
            max_value += amplitude
            amplitude *= self.persistence
            frequency *= self.lacunarity

        normalized = (total / max_value + 1) / 2
        return normalized * self.amplitude

    def get_scaled(self, x, y, min_val, max_val):
        """
        Retorna el valor del ruido escalado a un rango definido.
        Ej: get_scaled(x, y, 0.15, 0.85)
        """
        base_value = self.get(x, y)  # ya está entre [0, self.amplitude]
        normalized = base_value / self.amplitude if self.amplitude != 0 else 0.5
        return min_val + normalized * (max_val - min_val)

