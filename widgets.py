from kivy.uix.button import Button
from kivy.properties import ListProperty
from kivy.graphics import Color, RoundedRectangle


class RoundButton(Button):

    bg_color = ListProperty([0.2, 0.2, 0.2, 1])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.background_normal = ""
        self.background_down = ""
        self.background_color = (0, 0, 0, 0)

        with self.canvas.before:
            self.bg = Color(*self.bg_color)
            self.rect = RoundedRectangle(radius=[25])

        self.bind(pos=self.update_canvas,
                  size=self.update_canvas,
                  bg_color=self.update_color)

    def update_canvas(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def update_color(self, *args):
        self.bg.rgba = self.bg_color