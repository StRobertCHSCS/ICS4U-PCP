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

    def move(self):
        self.x = self.x + self.velocity_x
        self.y = self.y + self.velocity_y

    def update(self, dt):
        self.move()



class NameApp(App):
    def build(self):
        game = Background()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game

if __name__ == "__main__":
    NameApp().run()

