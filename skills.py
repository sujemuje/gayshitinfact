import random

import skill


class SkillQ(skill.BaseSkill):
    def __init__(self, player):
        super().__init__(player, 2, 'radi.png', .3)

    def cast(self, mouse_x, mouse_y) -> None:
        self.player.game.enemies.pop(random.randint(0, len(self.player.game.enemies) - 1))
        