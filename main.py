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
from random import *
from kivy.config import Config


Config.set('graphics','resizable',0) #prevents the app from being resizable

Window.clearcolor = (0,0,0,1.)


#create classes

class WidgetDrawer(Widget):
    #this draws all other widgets on the screen
    #includes movement, size, positioning
    #when a WidgetDrawer object is created, an image string is required
    def __init__(self, imageStr, **kwargs):
        super(WidgetDrawer, self).__init__(**kwargs)

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
        l.y = Window.height * 0.8
        self.add_widget(l)

        self.xwing = XWing(imageStr='./ship.png')
        self.xwing.x = Window.width / 4
        self.xwing.y = Window.height / 2
        self.add_widget(self.xwing)

    def addObstacle(self):
        imageNumber = randint(1, 6)
        imageStr = './obstacle_' + str(imageNumber) + '.png'
        tmpObstacle = Obstacle(imageStr)
        tmpObstacle.x = Window.width*0.99

        ypos = randint(1, 16)
        ypos = ypos*Window.height*0.625
        tmpObstacle.y = ypos
        tmpObstacle.y_velocity = 0
        vel = 10
        tmpObstacle.x_velocity =  -0.1 * vel

        self.obstacleList.append(tmpObstacle)
        self.add_widget(tmpObstacle)

    def on_touch_down(self, touch):
        self.xwing.impulse = 3
        self.xwing.g = -0.1

    def gameOver(self):
        restartButton = MyButton(text = 'Restart')
        def restart_button(obj):
            print 'restart button pushed'
            for obstacle in self.obstacleList:
                self.remove_widget(obstacle)
                self.xwing.xpos = Window.width * 0.25
                self.xwing.ypos = Window.height * 0.5
                self.probability = 1600

            self.obstacleList = []
            self.parent.remove_widget(restartButton)
            Clock.unschedule(self.update)
            Clock.schedule_interval(self.update, 1.0/60.0)
        restartButton.size = (Window.width * .3, Window.width * .1)
        restartButton.pos = Window.width * 0.5 - restartButton.width / 2, Window.height * 0.5
        restartButton.bind(on_release = restart_button)
        self.parent.add_widget(restartButton)

    def update(self, dt):
        self.xwing.update()
        tmpCount = randint(1, 1800)
        if tmpCount > self.probability:
            self.addObstacle()
            if self.probability < 1300:
                self.probability = 1300
            self.probability = self.probability - 1

        for obstacle in self.obstacleList:
            if obstacle.collide_widget(self.xwing):
                print 'Death'
                self.gameOver()
                Clock.unschedule(self.update)
            obstacle.update()
class ClientApp(App):

    def build(self):
        parent = Widget()
        app = GUI()
        Clock.schedule_interval(app.update, 1.0/60.0)
        parent.add_widget(app)
        return parent

if __name__ == '__main__' :
    ClientApp().run()









