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
    background = ObjectProperty(Image())

    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def update(self, dt):
        self.background.pos = Vector(*self.velocity) + self.background.pos
        self.background.pos = Vector(*self.velocity) + self.background.pos
        if self.background.right <= 0:
            self.backgroung.pos = (self.width, 0)

class Game(Widget):
    background = ObjectProperty(Background())

    def __init__(self):
        self.background.velocity = [-2, 0]

    def update(self):
        self.background.update()

class NameApp(App):
    def build(self):
        game = Game()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game

if __name__ == "__main__":
    NameApp().run()

