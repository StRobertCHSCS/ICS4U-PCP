__author__ = "Justin", "Danny"

import kivy
import random
import sys
kivy.require("1.8.0")

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

class NameApp(App):
    def build(self):
        game = Background()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game

NameApp().run()