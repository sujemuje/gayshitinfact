from pygame.math import Vector2 as Vec


class BaseEntity:
    def __init__(self, x, y, hp, atk, vel):
        self.pos = Vec(x, y)
        self.hp = hp
        self.atk = atk
        self.base_vel = vel
        self.vel_mod = 1

    def movable(self):
        return True
