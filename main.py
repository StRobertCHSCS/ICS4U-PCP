import kivy
kivy.require('1.7.2')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.properties import NumericProperty
from kivy.properties import ObjectProperty
from kivy.clock import Clock

from kivy.graphics import Rectangle, Color, Canvas
from functools import partial
from random import *

#setup graphics
from kivy.config import Config
Config.set('graphics','resizable',0)

#Graphics fix
from kivy.core.window import Window;
Window.clearcolor = (0,0,0,1.)
#Window.clearcolor = (1,0,0,1.)

class MyButton(Button):
#class used to get uniform button styles
    def __init__(self, **kwargs):
        super(MyButton, self).__init__(**kwargs)
        self.font_size = Window.width*0.018


class SmartMenu(Widget):
#instance of this class will appear when game starts for the first time
    buttonList = []

    def __init__(self, **kwargs):
    #create custom events first
        self.register_event_type('on_button_release')
        #will pass information from menu to parent instance
        super(SmartMenu, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation = 'vertical')
        self.layout.width = Window.width/2
        self.layout.height = Window.height/2
        self.layout.x = Window.width/2 - self.layout.width/2
        self.layout.y = Window.height/2 - self.layout.height/2
        self.add_widget(self.layout)


    def on_button_release(self, *args):
        pass


    def callback(self,instance):
        self.buttonText = instance.text
        self.dispatch('on_button_release') #tells parent instance to read button text


    def addButtons(self):
        for k in self.buttonList:
            tmpBtn = MyButton(text = k)
            tmpBtn.background_color = [.4, .4, .4, .4]
            tmpBtn.bind(on_release=self.callback) #button release, callback function is called
            self.layout.add_widget(tmpBtn)

    def buildUp(self):
        self.addButtons()

class SmartStartMenu(SmartMenu):
#button menu names
    buttonList = ['start', 'about']

    def __init__(self, **kwargs):
        super(SmartStartMenu, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation = 'vertical')
        self.layout.width = Window.width/2
        self.layout.height = Window.height/2
        self.layout.x = Window.width/2 - self.layout.width/2
        self.layout.y = Window.height/2 - self.layout.height/2
        self.add_widget(self.layout)

        self.msg = Label(text = 'Kessel Run')
        self.msg.font_size = Window.width*0.07
        self.msg.pos = (Window.width*0.45,Window.height*0.75)
        self.add_widget(self.msg)
        self.img = Image(source = 'lens2.png')
        self.img.size = (Window.width*1.5,Window.height*1.5)
        self.img.pos = (-Window.width*0.2,-Window.height*0.2)
        self.img.opacity = 0.35
        self.add_widget(self.img)

class WidgetDrawer(Widget):
#This widget is used to draw all of the objects on the screen, handles movement, size, and positioning
    def __init__(self, imageStr, **kwargs):
        super(WidgetDrawer, self).__init__(**kwargs)
        with self.canvas:
            self.size = (Window.width*.002*25,Window.width*.002*25)
            self.rect_bg=Rectangle(source=imageStr,pos=self.pos,size = self.size)
            self.bind(pos=self.update_graphics_pos)
            self.x = self.center_x
            self.y = self.center_y
            self.pos = (self.x, self.y)
            self.rect_bg.pos = self.pos

    def update_graphics_pos(self, instance, value):
        self.rect_bg.pos = value

    def setSize(self, width, height):
        self.size = (width, height)

    def setPos(self, xpos, ypos):
        self.x = xpos
        self.y = ypos




class Asteroid(WidgetDrawer):

    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    def move(self):
        self.x += self.velocity_x
        self.y += self.velocity_y

    def update(self):
        self.move()


class Ship(WidgetDrawer):

    impulse = 3
    grav = -0.1

    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    flameSize = (Window.width*.03,Window.width*.03)

    def move(self):
        self.x = self.x + self.velocity_x
        self.y = self.y + self.velocity_y

        #do not let ship stray too far
        if self.y < Window.height*0.05:
        #give upwards impulse
            self.impulse = 1
            self.grav = -0.1

        if self.y > Window.height*0.95:
            self.impulse = -3



    def determineVelocity(self):
        self.grav = self.grav*1.05
        if self.grav < -4:
            self.grav = -4
    #ship has a property called impulse
    #which is added whenever the player touches to calculate a and v of the ship

        self.velocity_y = self.impulse + self.grav
        self.impulse = 0.95*self.impulse

    def drawArrow(self, *largs):
        with self.canvas:
            flamePos = (self.pos[0]-Window.width*.02,self.pos[1]+Window.width*.01)

            flameRect = Rectangle(source='./flame.png',pos=flamePos, size = self.flameSize)

            def removeArrows(arrow, *largs):
                self.canvas.remove(arrow)
            Clock.schedule_once(partial(removeArrows, flameRect), .5)
            Clock.schedule_once(partial(self.updateArrows, flameRect), 0.1)

    def updateArrows(self,arrow,dt):
        with self.canvas:
            arrow.pos = (arrow.pos[0]-10,arrow.pos[1])

            Clock.schedule_once(partial(self.updateArrows, arrow), 0.1)
        return

    def explode(self):
    #create explosion 1
        tmpSize = Window.width*0.25,Window.width*0.2
        tmpPos = (self.x-Window.width*0.095, self.y-Window.width*0.08)
        with self.canvas: #create an explosion image,
            self.explosionRect = Rectangle(source ='./explosion1.png',pos=tmpPos,size=tmpSize)
        def changeExplosion(rect, newSource, *largs):
            rect.source = newSource

            #schedule explosion two
        Clock.schedule_once(partial(changeExplosion, self.explosionRect, './explosion2.png'), 0.2)
            #schedule explosion three
        Clock.schedule_once(partial(changeExplosion, self.explosionRect, './explosion3.png'), 0.4)
            #schedule explosion four
        Clock.schedule_once(partial(changeExplosion, self.explosionRect, './explosion4.png'), 0.6)
        Clock.schedule_once(partial(changeExplosion, self.explosionRect, './explosion5.png'), 0.8)

        def removeExplosion(rect, *largs):
            self.canvas.remove(rect) #remove the explosion drawing
        Clock.schedule_once(partial(removeExplosion, self.explosionRect), 1)

    def update(self):
        self.determineVelocity()
        self.move()

class GUI(Widget):
#this is the main widget that contains the game. Primary object that runs
    asteroidList =[]
#use numericproperty here so we can bind a callback to use every time the # changes
    asteroidScore = NumericProperty(0)
    def __init__(self, **kwargs):
        super(GUI, self).__init__(**kwargs)

        #setup label for the score
        self.score = Label(text = '0')
        self.score.y = Window.height*0.8
        self.score.x = Window.width*0.2

        def check_score(self,obj):
            #update credits
            self.score.text = str(self.asteroidScore)

        self.bind(asteroidScore = check_score)
        self.add_widget(self.score)

        #now we create a ship object
        self.ship = Ship(imageStr='./ship.png')
        self.ship.x = Window.width/4
        self.ship.y = Window.height/2
        self.add_widget(self.ship)

        Clock.schedule_interval(self.ship.drawArrow, 0.1)
    def addAsteroid(self):
    # add an asteroid to the screen
        imageNumber = randint(1, 4)
        imageStr = './obstacle_' + str(imageNumber) + '.png'
        tmpAsteroid = Asteroid(imageStr)
        tmpAsteroid.x = Window.width * 0.99

    # randomize y position
        ypos = randint(1, 16)

        ypos = ypos * Window.height * .0625

        tmpAsteroid.y = ypos
        tmpAsteroid.velocity_y = 0
        vel = 55
        tmpAsteroid.velocity_x = -0.1 * vel

        self.asteroidList.append(tmpAsteroid)
        self.add_widget(tmpAsteroid)

    def drawTouchResponse(self, x, y):
        # draw the arrows directly onto the canvas
        with self.canvas:
            tmpSize = Window.width * 0.07, Window.width * 0.07
            tmpPos = (x - self.width / 4, y - self.height / 4)
            self.arrowRect = Rectangle(source='./flame1.png', pos=tmpPos, size=tmpSize)

        # schedule removal
        def removeArrows(arrow, *largs):
            self.canvas.remove(arrow)

        def changeExplosion(rect, newSource, *largs):
            rect.source = newSource

        # schedule explosion two
        Clock.schedule_once(partial(changeExplosion, self.arrowRect, './flame2.png'), 0.15)
        # schedule explosion three
        Clock.schedule_once(partial(changeExplosion, self.arrowRect, './flame3.png'), 0.3)
        # schedule explosion four
        Clock.schedule_once(partial(changeExplosion, self.arrowRect, './flame4.png'), 0.45)
        Clock.schedule_once(partial(removeArrows, self.arrowRect), 0.6)

    # handle input events
    def on_touch_down(self, touch):
        self.ship.impulse = 3
        self.ship.grav = -0.1
        self.drawTouchResponse(touch.x, touch.y)

    def showScore(self):
        # this function will draw the score keeping widget, and rank with stars at death
        self.scoreWidget = ScoreWidget()
        self.scoreWidget.asteroidScore = self.asteroidScore  # pass on score
        self.scoreWidget.prepare()
        self.add_widget(self.scoreWidget)

    def removeScore(self):
        self.remove_widget(self.scoreWidget)

    def gameOver(self):
        # add a restart button
        restartButton = MyButton(text='Try Again')

        # restartButton.background_color = (.5,.5,1,.2)
        def restart_button(obj):
            # reset game
            self.removeScore()

            for k in self.asteroidList:
                self.remove_widget(k)
                self.ship.xpos = Window.width * 0.25
                self.ship.ypos = Window.height * 0.5
                self.minProb = 1780
                self.asteroidScore = 0
                self.asteroidList = []

            self.parent.remove_widget(restartButton)
            Clock.unschedule(self.update)
            Clock.schedule_interval(self.update, 1.0 / 60.0)
            restartButton.size = (Window.width * .3, Window.width * .1)
            restartButton.pos = Window.width * 0.5 - restartButton.width / 2, Window.height * 0.53
            restartButton.bind(on_release=restart_button)

            self.parent.add_widget(restartButton)


    def update(self, dt):
        # main update function for the game
        # All game logic and events originate from here

        # update game objects
        self.ship.update()

        # update asteroids
        # randomly add an asteroid
        tmpCount = randint(1, 15)
        prob = 1
        if tmpCount == prob:
            self.addAsteroid()

        for k in self.asteroidList:
            # check for collision with ship
            if k.collide_widget(self.ship):
                # game over routine
                self.gameOver()
                Clock.unschedule(self.update)
                # add reset button
                self.ship.explode()
            k.update()
        # check to see if asteroid is off of screen
            if k.x < -100:
                self.remove_widget(k)
                self.asteroidScore += 1
                tmpAsteroidList = self.asteroidList
                tmpAsteroidList[:] = [x for x in tmpAsteroidList if (x.x > -100)]
                self.asteroidList = tmpAsteroidList


class ClientApp(App):
    def build(self):
        self.parent = Widget()
        self.app = GUI()
        self.sm = SmartStartMenu()
        self.sm.buildUp()

        def check_button(obj):
            # check to see which button was pressed
            if self.sm.buttonText == 'start':
                # remove menu
                self.parent.remove_widget(self.sm)
                # start game
                Clock.unschedule(self.app.update)
                Clock.schedule_interval(self.app.update, 1.0 / 60.0)
                try:
                    self.parent.remove_widget(self.aboutText)
                except:
                    pass
            if self.sm.buttonText == 'about':
                self.aboutText = Label(text=('Created by Ryan Choi'))
                self.aboutText.pos = (Window.width * 0.45, Window.height * 0.35)
                self.parent.add_widget(self.aboutText)
                # bind a callback function that repsonds to event 'on_button_release' by calling function check_button

        self.sm.bind(on_button_release=check_button)
        # setup listeners for smartstartmenu
        self.parent.add_widget(self.sm)
        self.parent.add_widget(self.app)  # use this hierarchy to make it easy to deal w/buttons
        return self.parent


if __name__ == '__main__':
    ClientApp().run()


