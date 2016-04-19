__author__ = "Justin", "Danny"

import kivy
kivy.require("1.8.0")

from random import randint
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

    def __init__(self, **kwarg):
        super(Background, self).__init__(**kwarg)
        self.size = (800, 600)

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


class PlayerObj(Image):
    def __init__(self, pos):

        #placeholder image
        self.allow_stretch = True
        self.source = "images/Rock.gif"
        self.size = (60, 60)
        super(PlayerObj, self).__init__(pos=pos)

        self.velocity_y = 0
        self.gravity = 0.1

    def update(self):
        if self.velocity_y >= -2.7:
            self.velocity_y -= self.gravity
        self.y += self.velocity_y

    def on_touch_down(self, *ignore):
        if self.velocity_y <= 3.5:
            self.velocity_y += 8


class Obstacle(Image):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    marked = BooleanProperty(False)

    def __init__(self, **kwargs):
        super(Obstacle, self).__init__(**kwargs)

    def update(self):
        self.pos = Vector(*self.velocity) + self.pos


class Game(Widget):
    background = ObjectProperty(Background())
    obstacles = ListProperty([])

    def __init__(self, **kwargs):
        super(Game, self).__init__(**kwargs)

        self.background.velocity = [-0.25, 0]
        self.background.velocity = [-1, 0]
        self.bind(size=self.size_callback)
        self.size = Background().size

        #player's object
        self.player = PlayerObj(pos=(self.width / 4, self.height / 2))
        self.add_widget(self.player)

        #obstacle
        self.obstacle = Obstacle(pos=(self.width / 4, self.height / 2))
        self.add_widget(self.obstacle)

        Clock.schedule_interval(self.update, 1.0/1000.0)

    def remove_obstacle(self):
        self.remove_widget(self.obstacles[0])
        self.obstacles = self.obstacles[1:]

    def new_obstacle(self, remove=True):
        if remove:
            self.remove_obstacle()
        new_obstacle = Obstacle()
        new_obstacle.height = self.height
        new_obstacle.x = self.width
        new_obstacle.update_position()
        new_obstacle.velocity = [-3, 0]
        self.add_widget(new_obstacle)
        self.obstacles = self.obstacles + [new_obstacle]

    def size_callback(self, instance, value):
        for obstacle in self.obstacles:
            obstacle.height = value[1]
        self.background.size = value
        self.background.update_position()

    def update(self):
        self.background.update()
        self.player.update()
        for obstacle in self.obstacles:
            obstacle.update()
            if obstacle.x < self.player.x:
                self.new_obstacle(remove=False)
        if len(self.obstacles) == 0:
            self.new_obstacle(remove=False)
        elif self.obstacles[0].x < 0:
            self.remove_obstacle()


class NameApp(App):
    def build(self):
        game = Game()
        Clock.schedule_interval(game.update, 1.0 / 1000.0)
        return game

if __name__ == "__main__":
    NameApp().run()

