import heapq


class m_ai_logic:
    """
    Conjunto de comportamientos sencillos para entidades manejadas por IA
    (perseguir, huir, patrullar, deteccion de objetivos).
    """

    def __init__(self):
        pass

    def chase_target(self, enemy_pos, target_pos, speed):
        """
        Mueve una entidad hacia un objetivo.

        Args:
            enemy_pos (tuple): Posicion actual del enemigo (x, y).
            target_pos (tuple): Posicion del objetivo (x, y).
            speed (float): Velocidad de movimiento.

        Returns:
            tuple: Nueva posición (x, y) del enemigo.
        """
        dx = target_pos[0] - enemy_pos[0]
        dy = target_pos[1] - enemy_pos[1]
        dist = (dx**2 + dy**2) ** 0.5
        if dist == 0:
            return enemy_pos
        dx /= dist
        dy /= dist
        return enemy_pos[0] + dx * speed, enemy_pos[1] + dy * speed

    def flee_target(self, enemy_pos, threat_pos, speed):
        """
        Mueve una entidad alejandose de una amenaza.

        Args:
            enemy_pos (tuple): Posicion actual del enemigo (x, y).
            threat_pos (tuple): Posicion de la amenaza (x, y).
            speed (float): Velocidad de movimiento.

        Returns:
            tuple: Nueva posicion (x, y) del enemigo.
        """
        dx = enemy_pos[0] - threat_pos[0]
        dy = enemy_pos[1] - threat_pos[1]
        dist = (dx**2 + dy**2) ** 0.5
        if dist == 0:
            return enemy_pos
        dx /= dist
        dy /= dist
        return enemy_pos[0] + dx * speed, enemy_pos[1] + dy * speed

    def patrol(self, waypoints, current_index, position, speed):
        """
        Mueve una entidad siguiendo una lista de puntos de patrullaje en bucle.

        Args:
            waypoints (list): Lista de posiciones (x, y) que forman la ruta.
            current_index (int): Indice del punto objetivo actual en la ruta.
            position (tuple): Posicion actual (x, y) de la entidad.
            speed (float): Velocidad de movimiento.

        Returns:
            tuple: (nueva_posicion (x, y), nuevo_índice) de la ruta.
        """
        target = waypoints[current_index]
        dx = target[0] - position[0]
        dy = target[1] - position[1]
        dist = (dx**2 + dy**2) ** 0.5
        if dist < speed:
            current_index = (current_index + 1) % len(waypoints)
            target = waypoints[current_index]
            dx = target[0] - position[0]
            dy = target[1] - position[1]
            dist = (dx**2 + dy**2) ** 0.5
        dx /= dist
        dy /= dist
        new_pos = (position[0] + dx * speed, position[1] + dy * speed)
        return new_pos, current_index

    def can_see(self, pos_a, pos_b, max_distance):
        """
        Determina si dos posiciones están dentro de un rango de vision.

        Args:
            pos_a (tuple): Posicion del observador (x, y).
            pos_b (tuple): Posicion del objetivo (x, y).
            max_distance (float): Distancia maxima de vision.

        Returns:
            bool: True si el objetivo esta dentro del rango, False si no.
        """
        dx = pos_b[0] - pos_a[0]
        dy = pos_b[1] - pos_a[1]
        return (dx**2 + dy**2) <= max_distance**2


class m_priority_target_ai:
    """
    IA que selecciona objetivos segun un orden de prioridades.
    """
    def __init__(self, priorities):
        """
        priorities: lista de objetivos en orden de prioridad (strings), ejemplo:
        ["torreta", "generador", "jugador"]
        """
        self.priorities = priorities

    def select_target(self, visible_targets):
        """
        Selecciona el objetivo visible con mayor prioridad.

        Args:
            visible_targets (list): Lista de tuplas (nombre, datos_objetivo).

        Returns:
            tuple or None: El objetivo seleccionado o None si no hay coincidencias.
        """
        for priority in self.priorities:
            for target in visible_targets:
                if target[0] == priority:
                    return target
        return None

    def update_priorities(self, new_priorities):
        """
        Actualiza la lista de prioridades de la IA.

        Args:
            new_priorities (list): Nueva lista de prioridades.
        """
        self.priorities = new_priorities


class m_pathfinder:
    def __init__(self, is_walkable):
        """
        is_walkable(x, y): función que devuelve True si la posición es transitable
        """
        self.is_walkable = is_walkable

    def heuristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def get_neighbors(self, node):
        x, y = node
        neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        return [n for n in neighbors if self.is_walkable(n[0], n[1])]

    def reconstruct_path(self, came_from, current):
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        return path[::-1]

    def find_path(self, start, goal):
        open_set = []
        heapq.heappush(open_set, (0, start))
        came_from = {}
        g_score = {start: 0}
        f_score = {start: self.heuristic(start, goal)}

        while open_set:
            _, current = heapq.heappop(open_set)

            if current == goal:
                return self.reconstruct_path(came_from, current)

            for neighbor in self.get_neighbors(current):
                tentative_g = g_score[current] + 1
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score[neighbor] = tentative_g + self.heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

        return None
