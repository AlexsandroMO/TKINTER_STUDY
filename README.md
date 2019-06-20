# TKINTER_STUDY
Study  object orientation with Tkinter 
# Game Robot_Moviments
# By: Alexsandro Monteiro
# Date: 14/06/2019

from tkinter import *
from random import randint
import numpy as np
window = Tk()

# =============================
def call_button():
    start_again = Button(window, width=5, text="Start", command=bt_start)
    start_again.place(x=630, y=330)
    start_again['font'] = ('Arial', '10', 'bold')

def test_reward(positionX, positionY, test1X, test1Y, test2X, test2Y, test3X, test3Y):
    if positionX == test1X and positionY == test1Y and reward1.existe == True:
        print('O robô encontrou a moeda')

        reward_A = Label(window, text='X', bg='black', foreground="black")
        reward_A.place(x=reward1.x, y=reward1.y)
        reward_A['font'] = ('Arial', '20', 'bold')

        reward1.existe = False

        r1.ganhaponto()

        score = Label(window, text='Score: ' + str(r1.cont), bg='black', foreground='white')
        score.place(x=700, y=10)
        score['font'] = ('Arial', '10', 'bold')

    elif positionX == test2X and positionY == test2Y and reward2.existe == True:
        print('O robô encontrou a moeda')

        reward_B = Label(window, text='X', bg='black', foreground="black")
        reward_B.place(x=reward2.x, y=reward2.y)
        reward_B['font'] = ('Arial', '20', 'bold')

        reward2.existe = False

        r1.ganhaponto()

        score = Label(window, text='Score: ' + str(r1.cont), bg='black', foreground='white')
        score.place(x=700, y=10)
        score['font'] = ('Arial', '10', 'bold')

    elif positionX == test3X and positionY == test3Y and reward3.existe == True:
        print('O robô encontrou a moeda')

        reward_C = Label(window, text='X', bg='black', foreground="black")
        reward_C.place(x=reward3.x, y=reward3.y)
        reward_C['font'] = ('Arial', '20', 'bold')

        reward3.existe = False

        r1.ganhaponto()

        score = Label(window, text='Score: ' + str(r1.cont), bg='black', foreground='white')
        score.place(x=700, y=10)
        score['font'] = ('Arial', '10', 'bold')

# -------------------------------------
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

# -------------------------------------
class Reward(Point):
    def __init__(self, x, y):
        super(Reward, self).__init__(x, y)
        self.existe = True

# -------------------------------------
class Robot(Point):
    def __init__(self, x, y, cont):
        self.x = x
        self.y = y
        self.cont = cont

    def ganhaponto(self):
        self.cont += 1
        if self.cont == 3:
            self.win = Label(window, text='You Win!', bg='black', foreground='white')
            self.win.pack()
            self.win['font'] = ('Arial', '30', 'bold')

    def move_down(self):  # Invertido
        if self.y < 400:
            self.y = self.y + 20
        else:
            print('O Robo chegou o fim da tela')

    def move_up(self):  # Invertido
        if self.y > 0:
            self.y = self.y - 20

        else:
            print('O Robo chegou o fim da tela')

    def move_right(self):
        if self.x < 750:
            self.x = self.x + 20
        else:
            print('O Robo chegou o fim da tela')

    def move_left(self):
        if self.x > 0:
            self.x = self.x - 20
        else:
            print('O Robo chegou o fim da tela')


# -------------------------------------

r1 = Robot(440, 240, 0)
reward1 = Reward(500, 200)
reward2 = Reward(500, 400)
reward3 = Reward(760, 200)

# ========================================

def bt_start():
    r1.x = 440
    r1.y = 240
    r1.cont = 0
    reward1.x = randint(0, 500)
    reward1.y = randint(0, 400)
    reward2.x = randint(0, 500)
    reward2.y = randint(0, 400)
    reward3.x = randint(0, 500)
    reward3.y = randint(0, 400)

    reward1.existe = True
    reward2.existe = True
    reward3.existe = True

    r1.win.destroy()

    reward_A = Label(window, text='X', bg='black', foreground="yellow")
    reward_A.place(x=reward1.x, y=reward1.y)
    reward_A['font'] = ('Arial', '20', 'bold')

    reward_B = Label(window, text='X', bg='black', foreground="blue")
    reward_B.place(x=reward2.x, y=reward2.y)
    reward_B['font'] = ('Arial', '20', 'bold')

    reward_C = Label(window, text='X', bg='black', foreground="red")
    reward_C.place(x=reward3.x, y=reward3.y)
    reward_C['font'] = ('Arial', '20', 'bold')

    score = Label(window, text='Score: ' + str(r1.cont), bg='black', foreground='white')
    score.place(x=700, y=10)
    score['font'] = ('Arial', '10', 'bold')

def bt_click_UP():

    if r1.cont < 3:
        r1.move_up()
        test_reward(r1.x, r1.y, reward1.x, reward1.y, reward2.x, reward2.y, reward3.x, reward3.y)
        print('X = ', r1.x)
        print('Y = ', r1.y)
        print(reward1.x , reward1.y , reward1.existe)

        robot.place(x=r1.x, y=r1.y)
        robot['font'] = ('Arial', '20', 'bold')


def bt_click_Down():
    if r1.cont < 3:
        r1.move_down()
        test_reward(r1.x, r1.y, reward1.x, reward1.y, reward2.x, reward2.y, reward3.x, reward3.y)
        print('X = ', r1.x)
        print('Y = ', r1.y)

        robot.place(x=r1.x, y=r1.y)
        robot['font'] = ('Arial', '20', 'bold')
    else:
        call_button()

def bt_click_Left():
    if r1.cont < 3:
        r1.move_left()
        test_reward(r1.x, r1.y, reward1.x, reward1.y, reward2.x, reward2.y, reward3.x, reward3.y)
        print('X = ', r1.x)
        print('Y = ', r1.y)

        robot.place(x=r1.x, y=r1.y)
        robot['font'] = ('Arial', '20', 'bold')

def bt_click_Right():
    if r1.cont < 3:
        r1.move_right()
        test_reward(r1.x, r1.y, reward1.x, reward1.y, reward2.x, reward2.y, reward3.x, reward3.y)
        print('X = ', r1.x)
        print('Y = ', r1.y)

        robot.place(x=r1.x, y=r1.y)
        robot['font'] = ('Arial', '20', 'bold')

# ---------------------------------

score = Label(window, text='Score: ' + str(r1.cont), bg='black', foreground='white')
score.place(x=700, y=10)
score['font'] = ('Arial', '10', 'bold')

robot = Label(window, text="O", bg='black', foreground="white")
robot.place(x=r1.x, y=r1.y)
robot['font'] = ('Arial', '20', 'bold')

reward_A = Label(window, text='X', bg='black', foreground="yellow")
reward_A.place(x=reward1.x, y=reward1.y)
reward_A['font'] = ('Arial', '20', 'bold')

reward_B = Label(window, text='X', bg='black', foreground='red')
reward_B.place(x=reward2.x, y=reward2.y)
reward_B['font'] = ('Arial', '20', 'bold')

reward_C = Label(window, text='X', bg='black', foreground='blue')
reward_C.place(x=reward3.x, y=reward3.y)
reward_C['font'] = ('Arial', '20', 'bold')

# -------------------------------------------------

bt_UP = Button(window, width=5, text="Up", command=bt_click_UP)
bt_UP.place(x=630, y=430)
bt_UP['font'] = ('Arial', '10', 'bold')

bt_Down = Button(window, width=5, text="Down", command=bt_click_Down)
bt_Down.place(x=630, y=470)
bt_Down['font'] = ('Arial', '10', 'bold')

bt_Left = Button(window, width=5, text="Left", command=bt_click_Left)
bt_Left.place(x=550, y=470)
bt_Left['font'] = ('Arial', '10', 'bold')

bt_Right = Button(window, width=5, text="Right", command=bt_click_Right)
bt_Right.place(x=710, y=470)
bt_Right['font'] = ('Arial', '10', 'bold')

# ------------------------------
window.wm_title("Robot Moviment")
window["bg"] = "black"
window.geometry("800x500")

window.mainloop()
