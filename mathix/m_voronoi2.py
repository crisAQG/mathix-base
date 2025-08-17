from mathix.m_algebra import *
from mathix.m_random import *


class m_voronoi2:
    def __init__(self, width, height, cell_size=1, num_points=10, min_distance=0, seed=None):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.cols = width // cell_size
        self.rows = height // cell_size
        self.num_points = num_points
        self.min_distance = min_distance
        self.points = []
        self.data = []
        self.seed = seed
        self.rng = m_random(self.seed)

    def _distance(self, x1, y1, x2, y2):
        return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    def _generate_points(self):
        """Genera puntos aleatorios con distancia mínima."""
        attempts = 0
        while len(self.points) < self.num_points and attempts < self.num_points * 50:
            px = self.rng.randint(0, self.cols - 1)
            py = self.rng.randint(0, self.rows - 1)

            if all(self._distance(px, py, x, y) >= self.min_distance for x, y in self.points):
                self.points.append((px, py))
            attempts += 1

        if len(self.points) < self.num_points:
            print("No se pudieron colocar todos los puntos con la distancia mínima indicada.")

    def generate(self, values=None):
        """
        Genera la matriz Voronoi.
        :param values: Lista opcional de valores asociados a cada punto.
                       Si no se pasa, se usa el índice del punto.
        :return: Matriz 2D de tamaño [rows][cols]
        """
        self._generate_points()

        if values is None:
            values = list(range(len(self.points)))

        self.data = []
        for y in range(self.rows):
            row = []
            for x in range(self.cols):
                min_dist = float('inf')
                nearest_index = 0
                for i, (px, py) in enumerate(self.points):
                    dist = self._distance(x, y, px, py)
                    if dist < min_dist:
                        min_dist = dist
                        nearest_index = i
                row.append(values[nearest_index])
            self.data.append(row)

        return self.data