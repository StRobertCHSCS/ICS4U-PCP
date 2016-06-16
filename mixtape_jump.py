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
"""
Class that initializes all the widgets used in this game.
"""
#This widget is used to draw all of the objects on the screen
#objects of this class must be initiated with an image string

    def __init__(self, imageStr, **kwargs):
    """
    Initializes widget movement, size, positioning
    :param imageStr: str - What allows you to put the location of your imported images
    :param kwargs: None
    :return: None
    """
        super(WidgetDrawer, self).__init__(**kwargs)

        with self.canvas:
        #this line creates a rectangle with the image drawn on top
            self.size = (Window.width*.005*25,Window.height*.005*25)
            self.rect_bg= Rectangle(source=imageStr,pos=self.pos,size = self.size)

            #this line calls the update_graphics_pos function every time the position variable is modified
            self.bind(pos=self.update_graphics_pos)
            self.x = self.center_x
            self.y = self.center_y

            #center the widget
            self.pos = (self.x,self.y)

            #center the rectangle on the widget
            self.rect_bg.pos = self.pos

    def update_graphics_pos(self, instance, value):
        """
        If the position of the widget is moved then the rectangle which has the image is also moved
        :param instance:
        :param value: int - What updates the rectangles position after the position of the widget has changed
        :return: None
        """
        #if the widgets position moves, the rectangle that contains the image is also moved
        self.rect_bg.pos = value

    #use this function to change widget size
    def setSize(self,width, height):
        """
        Set the size of the widgets
        :param width: int - The width of the widget
        :param height: int - The height of the widget
        :return: None
        """
        self.size = (width, height)

    def setPos(self,xpos,ypos):
        """
        Setting initial x and y positions of the widget
        :param xpos: int - X position of widget
        :param ypos: int - Y position of widget
        :return: None
        """
        self.x = xpos
        self.y = ypos


class rapper(WidgetDrawer):
    """
    Class that contains the rapper heads which the floating mixtape must avoid.
    """
    #update the position using the velocity defined here. every time move is called we change the position by velocity_x
    velocity_x = NumericProperty(0) #initialize velocity_x and velocity_y
    velocity_y = NumericProperty(0) #declaring variables is not necessary in python

    def move(self):
        """
        Adds a velocity to the rapper heads.
        :return: None
        """
        self.x = self.x + self.velocity_x
        self.y = self.y + self.velocity_y

    def update(self):
        """
        Updates the position of the rapper heads. They are now moving cause they have velocity.
        :return: None
        """
        self.move()