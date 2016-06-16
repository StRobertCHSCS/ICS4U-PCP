__author__ = 'Ryan'


#import everything I need for this game
import kivy
kivy.require('1.7.2')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.properties import NumericProperty
from kivy.clock import Clock
from kivy.graphics import Rectangle
from random import
from kivy.config import Config


Config.set('graphics','resizable',0) #prevents the app from being resizable

Window.clearcolor = (0,0,0,1.)


#create classes

class WidgetDrawer(Widget):
    #this draws all other widgets on the screen
    #includes movement, size, positioning
    #when a WidgetDrawer object is created, an image string is required
    def __init__(self, imageStr, **kwargs):
        super(WidgetDrawer, self).init(**kwargs)
        with self.canvas:
            self.size = (Window.width * .002 * 25, Window.width * .002 * 25)
            self.rect_bg = Rectangle(source=imageStr, pos=self.pos, size=self.size)
            self.bind(pos=self.update_graphics_pos)
            self.x = self.center_x
            self.y = self.center_y
            self.pos = (self.x, self.y)
            self.rect_bg.pos = self.pos

            def update_graphics_pos(self, instance, value):
                self.rect_bg.pos = value

            def setSize(self, width, height):
                self.size = (width, height)

            def setPos(xpos, ypos):
                self.x = xpos
                self.y = ypos
class Obstacle(WidgetDrawer):
    #obstacles the player will dodge
    x_velocity = NumericProperty(0)
    y_velocity = NumericProperty(0)
    def move(self):
        self.x = self.x + self.x_velocity
        self.y = self.y + self.y_velocity
    def update(self):
        self.move()

class XWing(WidgetDrawer):
    impulse = 3
    g = -0.1

    x_velocity = NumericProperty(0)
    y_velocity = NumericProperty(0)

    def move(self):
        self.x = self.x + self.x_velocity
        self.y = self.y + self.y_velocity

        if self.y is Window.height * 0.95:
            self.impulse = -3

    def Determine_Velocity(self):
        self.g = self.g *1.05
        if self.g < -4:
            self.g = -4
        self.velocity_y = self.impulse + self.g
        self.impulse = 0.95 * self.impulse

    def update(self):
        self.Determine_Velocity()
        self.move()

class GUI(Widget):
    obstacleList = []
    probability = 1500
    def __init__(self, **kwargs):
        super(GUI, self).__init__(**kwargs)
        l = Label(text = 'X-Wing Derp')
        l.x = Window.width/2 - l.width/2
        1.y = Window.height * 0.8
        self.add_widget(l)

        self.xwing = Ship(imageStr='./ship.png')
        self.xwing.x = Window.width / 4
        self.xwing.y = Window.height / 2
        self.add_widget(self.ship)

    def addObstacle(self):
        imageNumber = randint(1, 6)
