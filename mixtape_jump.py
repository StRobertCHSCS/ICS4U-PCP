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

class WidgetDrawer(Widget):

    def __init__(self, imageStr, **kwargs):
        super(WidgetDrawer, self).__init__(**kwargs)
        with self.canvas:

            self.size = (Window.width*.005*25,Window.height*.005*25)
            self.rect_bg= Rectangle(source=imageStr,pos=self.pos,size = self.size)

            self.bind(pos=self.update_graphics_pos)
            self.x = self.center_x
            self.y = self.center_y

            self.pos = (self.x,self.y)

            self.rect_bg.pos = self.pos

    def update_graphics_pos(self, instance, value):

        self.rect_bg.pos = value

    def setSize(self,width, height):
        self.size = (width, height)
    def setPos(self,xpos,ypos):
        self.x = xpos
        self.y = ypos


