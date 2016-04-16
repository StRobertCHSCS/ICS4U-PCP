__author__ = "Justin", "Danny"

import kivy
kivy.require("1.8.0")

import random
import sys

from kivy.properties import NumericProperty, ReferenceListProperty, BooleanProperty, ObjectProperty, ListProperty
from kivy.uix.image import Image
from kivy.vector import Vector
from kivy.app import App
from kivy.clock import Clock
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.widget import Widget




class Background(Widget):
    image1 = ObjectProperty(Image())
    image2 = ObjectProperty(Image())

    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def update(self):
        self.image1.pos = Vector(*self.velocity) + self.image1.pos
        self.image2.pos = Vector(*self.velocity) + self.image2.pos

        if self.image1.right <= 0:
            self.image1.pos = (self.width, 0)
        if self.image2.right <= 0:
            self.image2.pos = (self.width, 0)

    def update_position(self):
        self.image1.pos = (0, 0)
        self.image2.pos = (self.width, 0)

class PlayerObj(Widget):
    #placeholder image used
    player_image = ObjectProperty(Image())

    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def __init__(self, **kwargs):
        super(PlayerObj, self).__init__(**kwargs)

"""
    def on_touch_down(self, touch):
        self.jumping = True
        self.bird_image.source = "images/flappynormal.png"
        self.velocity_y = self.jump_height / (self.jump_time * 60.0)
        Clock.unschedule(self.stop_jumping)
        Clock.schedule_once(self.switch_to_normal, self.jump_time  / 5.0)
"""

class Game(Widget):
    background = ObjectProperty(Background())
    player = ObjectProperty(PlayerObj())

    #change window size below, can get rid of black stuff tho
    Window.size = (800, 600)

    def __init__(self, **kwargs):
        super(Game, self).__init__(**kwargs)
        self.background.velocity = [-1, 0]
        self.bind(size=self.size_callback)


    def size_callback(self, instance, value):
        self.background.size = value
        self.background.update_position()

    def update(self, dt):
        self.background.update()
        """
        self.player.update()
        """

class NameApp(App):
    def build(self):
        game = Game()
        Clock.schedule_interval(game.update, 1.0 / 100.0)
        return game
if __name__ == "__main__":
    NameApp().run()

