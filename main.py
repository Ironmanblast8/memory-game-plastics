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
    for fname in sh_names:
        screen.addshape(fname)

    face_up = [False ] * 9
    card_type = ["bag", "bottle", "net", "straw"] * 2
    card_type.append("fish")
    shuffle(card_type)
    card_pos = [(-200,-200),(0,-200),(200,-200),(-200,0),(0,0),(200,0),(-200,200),(0,200),(200,200)]
    cards = []
    for num in range(9):
        t = turtle.Turtle()
        t.front = card_type[num]
        t.shape("back.gif")
        t.goto(card_pos[num])
      
        cards.append(t)
        cards[num].shape(card_type[num]+".gif")


if __name__ == "__main__":
    init()
