import kivy
kivy.require('1.7.2')
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.properties import NumericProperty
from kivy.clock import Clock
from kivy.graphics import Rectangle, Color, Canvas
from random import *


class mixtape(WidgetDrawer):
   def __init__(self, imageStr) :
       WidgetDrawer.__init__(self, imageStr)
       self.impulse = 3
       self.grav = -0.1

       self.velocity_x = 0
       self.velocity_y = 0

       self.setSize(50, 30)

   def setSize (self, width, height):
       WidgetDrawer.setSize(self, width, height)

   def move(self):
       self.x = self.x + self.velocity_x
       self.y = self.y + self.velocity_y

       if self.y > Window.height*0.95:
           self.impulse = -3

   def determineVelocity(self):
       self.grav = self.grav*1.05
       if self.grav < -4:
           self.grav = -4

       self.velocity_y = self.impulse + self.grav
       self.impulse = 0.95*self.impulse

   def update(self):
       self.determineVelocity()
       self.move()


class MyButton(Button):

   def __init__(self, **kwargs):
       super(MyButton, self).__init__(**kwargs)
       self.font_size = Window.width*0.018

