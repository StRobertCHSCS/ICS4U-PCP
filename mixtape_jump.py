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

class GUI(Widget):
    rapperList =[]
    rapperScore = NumericProperty(0)
    minProb = 1780
    def __init__(self, **kwargs):
        super(GUI, self).__init__(**kwargs)
        self.score = Label(text = "0")
        self.score.y = Window.height*0.8
        self.score.x = Window.width*0.2
        self.rapperScore = 0
        l = Label(text='Mixtape Jump')
        l.x = Window.width/2 - l.width/2
        l.y = Window.height*0.8
        self.add_widget(l)
        self.mixtape = mixtape(imageStr = 'C:\Users\Koven\desktop\photoshopped\mmixtape.png')
        self.mixtape.x = Window.width/4
        self.mixtape.y = Window.height/2
        self.add_widget(self.mixtape)
    def check_score(self,obj):
            self.score.text = str(self.rapperScore)

        self.bind(rapperScore = check_score)
        self.add_widget(self.score)


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


