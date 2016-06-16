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