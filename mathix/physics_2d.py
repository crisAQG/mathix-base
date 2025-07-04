class physics_2d:
    def __init__(self, gravity=(0, 0.5), friction=0.9):
        self.gravity = gravity
        self.friction = friction

    def apply_gravity(self, velocity, gravity_scale=1.0):
        return (
            velocity[0] + self.gravity[0] * gravity_scale,
            velocity[1] + self.gravity[1] * gravity_scale
        )

    def apply_friction(self, velocity):
        return (
            velocity[0] * self.friction,
            velocity[1] * self.friction
        )

    def update_position(self, position, velocity):
        return (
            position[0] + velocity[0],
            position[1] + velocity[1]
        )

    def bounce(self, velocity, normal, elasticity=1.0):
        dot = velocity[0]*normal[0] + velocity[1]*normal[1]
        return (
            velocity[0] - (1 + elasticity) * dot * normal[0],
            velocity[1] - (1 + elasticity) * dot * normal[1]
        )

    def limit_speed(self, velocity, max_speed):
        mag = (velocity[0]**2 + velocity[1]**2) ** 0.5
        if mag > max_speed:
            scale = max_speed / mag
            return (velocity[0] * scale, velocity[1] * scale)
        return velocity

    def handle_piercing(self, projectile):
        projectile.pierced_count += 1
        if projectile.pierced_count >= projectile.max_pierces:
            projectile.active = False
