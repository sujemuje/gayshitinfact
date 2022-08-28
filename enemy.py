import entity


class Enemy(entity.BaseEntity):
    def __init__(self, x, y, hp, atk, vel):
        super().__init__(x, y, hp, atk, vel)