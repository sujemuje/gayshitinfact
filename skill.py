import arcade


class Skill:
    def __init__(self, cd, icon_file_name, *a, **kw):
        self.cd = cd
        self.icon = arcade.Sprite(icon_file_name, *a, **kw)
        self.icon.set_position(100, 100)

    def on_draw(self, i) -> None:
        self.icon.draw()
        arcade.draw_arc_filled(100, 100, 100, 100, (0xff, 0x00, 0x00), 45, 360, num_segments=360)
