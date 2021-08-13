# memory game for platics in waterways / oceans
import turtle
from time import sleep
from random import shuffle


def init():
    screen = turtle.Screen()
    screen.title('Memory game match plastic in the ocean to remove')
    screen.bgcolor("CornFlowerBlue")
    sh_names = ["bag.gif", "bottle.gif", "net.gif", "straw.gif"]
    screen.addshape("back.gif")
    screen.addshape("fish.gif")
    for fname in sh_names:
        screen.addshape(fname)

    face_up = [False ] * 9
    card_type = ["bag", "bottle", "net", "straw"] * 2
    card_type.append("fish")
    shuffle(card_type)
    card_pos = [(-135,-135),(0,-135),(135,-135),(-135,0),(0,0),(135,0),(-135,135),(0,135),(135,135)]
    numb_pos = [(-200,-200),(65,-200),(200,-200),(-200,65),(-200,200),(-200,65)]

    cards = []
    for num in range(9):
        t = turtle.Turtle()
        t.front = card_type[num]
        t.shape("back.gif")
        t.penup()
        t.goto(card_pos[num])
        sleep(1)
        cards.append(t)
        # cards[num].shape(card_type[num]+".gif")

    numb = []
    for num in range(6):
      t = turtle.Turtle()
      t.penup()
      t.goto(numb_pos[num])
      t.pendown()
      t.write ("1")


if __name__ == "__main__":
    init()
