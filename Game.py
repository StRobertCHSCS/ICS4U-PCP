import kivy
from kivy.properties import NumericProperty, ReferenceListProperty, BooleanProperty, ObjectProperty, ListProperty
from kivy.uix.image import Image
from kivy.vector import Vector
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.widget import Widget
import random
import sys


class Background(Widget):
    image1 = ObjectProperty(Image())
    image2 = ObjectProperty(Image())

    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def __init__(self, **kwarg):
        super(Background, self).__init__(**kwarg)
        self.allow_stretch = True
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

        # image properties
        self.allow_stretch = True

        self.source = "images/Box.gif"
        self.size = (60, 60)

        super(PlayerObj, self).__init__(pos=pos)

        self.anim_delay = 0.25
        self.velocity_y = 0
        self.gravity = 0.06

    def update(self):

        if self.velocity_y >= -3:
            self.velocity_y -= self.gravity
        self.y += self.velocity_y

    def on_touch_down(self, *ignore):
        self.velocity_y = 4


class PlayerHB(Widget):
    def __init__(self, pos):

        super(PlayerHB, self).__init__(pos=pos)
        self.size = (10, 10)


class Obstacle(Image):
    def __init__(self, pos):
        self.allow_stretch = False
        self.source = "images/one_pillar.png"
        self.size = (70,650)

        super(Obstacle, self).__init__(pos=pos)

        self.velocity_x = -1.5

    def update(self):
        self.x += self.velocity_x


class Game(Widget):
    background = ObjectProperty(Background())

    def __init__(self, **kwargs):

        super(Game, self).__init__(**kwargs)
        self.background.anim_delay = 0.05
        self.background.velocity = [-0.25, 0]
        self.bind(size=self.size_callback)
        self.size = Background().size




        # player's object - the rock
        self.player = PlayerObj(pos=(self.width / 4, self.height / 2))
        self.add_widget(self.player)

        self.playerhb = PlayerHB(pos=(self.player.center_x-0.5*35, self.player.center_y))
        self.add_widget(self.playerhb)


        # obstacle
        x = random.randint(250, 750)
        self.obstacle1 = Obstacle(pos=(900, -x))
        self.obstacle2 = Obstacle(pos=(1400, -x))
        self.add_widget(self.obstacle1)
        self.add_widget(self.obstacle2)

        # score
        self.score = 0
        self.score_bool = False
        self.scorelabel = Label(pos=(self.width * 2.2 / 3, self.height / 4 * 3.2), text="[size=40][color=ff3333]{0}[/color][/size]".format(str(self.score)), markup=True, )
        self.add_widget(self.scorelabel)

        Clock.schedule_interval(self.update, 1.0 / 60.0)




    def size_callback(self, instance, value):
        self.background.size = value
        self.background.update_position()

    def update(self, dt):
        # collision stuff

        if self.player.y <= 0:
            self.player.y = 0
        elif self.player.y >= self.height - self.player.height:
            self.player.y = self.height - self.player.height
            self.player.velocity_y = 0

        self.playerhb.center_x = self.player.center_x
        self.playerhb.center_y = self.player.center_y

        # collision; the shape of the widgets needs to change to accurately reflect the collision

        if self.playerhb.collide_widget(self.obstacle1) or self.playerhb.collide_widget(self.obstacle2):

            print "hit"
        else:
            print "no"
        # update calls
        self.background.update()
        self.player.update()

        self.obstacle1.update()
        self.obstacle2.update()

        # obstacle movement

        if self.obstacle1.x + self.obstacle1.width <= 0:
            x = random.randint(250, 750)
            self.remove_widget(self.obstacle1)
            self.obstacle1 = Obstacle(pos=(900, -x))
            self.add_widget(self.obstacle1)
            self.score_bool = False

        if self.obstacle2.x + self.obstacle2.width <= 0:
            x = random.randint(250, 750)
            self.remove_widget(self.obstacle2)
            self.obstacle2 = Obstacle(pos=(900, -x))
            self.add_widget(self.obstacle2)
            self.score_bool = False

        # get obstacle pos in order to increase score instead of just this for testing, score update call
        if self.player.x >= self.obstacle1.x and self.score_bool == False:
            self.score_bool = True
            self.score += 1

        if self.player.x >= self.obstacle2.x and self.score_bool == False:
            self.score_bool = True
            self.score += 1

        self.scorelabel.text = "[size=40][color=0266C9]{0}[/color][/size]".format(str(self.score))


class NameApp(App):
    def build(self):
        game = Game()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game


if __name__ == "__main__":
    NameApp().run()
