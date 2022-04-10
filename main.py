from tkinter import *
import pygame
import random
from graphics import *
import turtle as tur

root = Tk()
root.title('Projekt 1')
root.geometry("600x400")


def obrazek():
    tur.speed(0.38)
    screen =  tur.Screen()
    screen.setup(660,550)
    screen.cv._rootwindow.resizable(False, False)
    tur.bgcolor('green')
    tur.hideturtle()
    tur.penup()
    tur.goto(-400, -100)
    tur.pendown()
    tur.color("deepskyblue")
    tur.begin_fill()
    for i in range(2):
        tur.forward(800)
        tur.left(90)
        tur.forward(500)
        tur.left(90)
    tur.end_fill()
    tur.penup()
    tur.begin_fill()
    tur.color('brown')
    tur.goto(-105,-101)
    tur.pendown()
    tur.left(90)
    for i in range(3):
        tur.forward(180)
        tur.right(90)
    tur.penup()

    tur.end_fill()
    tur.goto(-125, 50)
    tur.right(180)
    tur.pendown()
    tur.begin_fill()
    for i in range(3):
        tur.color("orange")
        tur.forward(225)
        tur.left(120)
    tur.penup()
    tur.end_fill()

    tur.color("saddle brown")
    tur.goto(-40,-101)
    tur.pendown()
    tur.begin_fill()
    tur.left(90)
    tur.forward(60)
    tur.right(90)
    tur.forward(40)
    tur.right(90)
    tur.forward(60)
    tur.end_fill()
    tur.penup()

    tur.right(90)
    tur.forward(200)
    tur.right(90)
    tur.forward(300)
    tur.pendown()
    tur.color("yellow")
    tur.begin_fill()
    tur.circle(35)
    tur.end_fill()
    tur.done()
def beizer():
    punktyx = [100, 100, 100, 100]
    punktyy = [500, 500, 100, 100]

    punktyx2 = [100, 300, 300, 100]
    punktyy2 = [100, 100, 300, 300]

    punktyx3 = [400, 400, 400, 400]
    punktyy3 = [100, 100, 500, 500]

    punktyx4 = [400, 400, 600, 600]
    punktyy4 = [300, 300, 450, 500]

    punktyx5 = [400, 450, 650, 600]
    punktyy5 = [300, 350, 150, 100]

    okno = GraphWin("Krzywe Beizera", 800, 800)

    def beizer(punktyx, punktyy):
        t = 0

        for x in range(3):
            c = Point(punktyx[x], punktyy[x])
            c.draw(okno)

        for z in range(1000):
            rysuj_x = pow(1 - t, 3) * punktyx[0] + 3 * t * pow(1 - t, 2) * punktyx[1] + 3 * t * t * (1 - t) * punktyx[
                2] + pow(t, 3) * punktyx[3]
            rysuj_y = pow(1 - t, 3) * punktyy[0] + 3 * t * pow(1 - t, 2) * punktyy[1] + 3 * t * t * (1 - t) * punktyy[
                2] + pow(t, 3) * punktyy[3]
            d = Point(rysuj_x, rysuj_y)
            d.draw(okno)
            t += 0.001

    beizer(punktyx, punktyy)
    beizer(punktyx2, punktyy2)
    beizer(punktyx3, punktyy3)
    beizer(punktyx4, punktyy4)
    beizer(punktyx5, punktyy5)
    okno.getMouse()
    okno.close()


def gra():
    pygame.init()
    win = pygame.display.set_mode((500, 600))
    rozowy = (139, 0, 139)
    zielony = (130, 175, 55)
    bialy = (255, 255, 255)
    punkty = 0
    font = pygame.font.Font('freesansbold.ttf', 24)
    text = font.render('Punkty: ' + str(punkty), True, rozowy, zielony)
    textRect = text.get_rect()
    text2 = font.render('KONIEC', True, rozowy, zielony)
    textRect2 = text.get_rect()
    pygame.display.set_caption("MegaTibia BETA")
    x = 200
    y = 200
    width = 20
    height = 20
    blok = 20
    lastx = 0
    lasty = 0
    run = True
    display_surface = pygame.display.set_mode((500, 600))
    textRect.center = (250, 560)

    background_image = pygame.image.load("tlo1.png").convert()

    # WKLEJONE

    x1 = 260
    y1 = 300

    x1_change = 0
    y1_change = 0
    snake_block = 20
    snake_blocks = []
    snake_len = 5

    def our_snake(snake_block, snake_list):
        for x in snake_list:
            pygame.draw.rect(win, rozowy, [x[0], x[1], snake_block, snake_block])


    szybkosc = 10
    polex = random.randrange(20, 460, 20)
    poley = random.randrange(20, 460, 20)
    Ostatni = "Up"
    clock = pygame.time.Clock()
    kolor = (65, 32, 82)
    while run:

        display_surface.blit(background_image, [0, 0])

        t = 0
        for x in range(27):
            pygame.draw.line(win, kolor, (20, -1 + t), (480, -1 + t), 1)
            pygame.draw.line(win, kolor, (0 + t, 20), (t, 520), 1)
            t += 20

        text = font.render('Punkty: ' + str(punkty), True, rozowy)
        text.set_alpha(127)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and x1 > 0:

            if (Ostatni == "Right"):
                Ostatni = "Right"
            else:
                Ostatni = "Left"

        if keys[pygame.K_RIGHT] and x1 < 500 - width:
            # x += vel
            if (Ostatni == "Left"):
                Ostatni = "Left"
            else:
                Ostatni = "Right"

        if keys[pygame.K_UP] and y1 > 0:
            if (Ostatni == "Down"):
                Ostatni = "Down"
            else:
                Ostatni = "Up"

        if keys[pygame.K_DOWN] and y1 < 500 - height:
            if (Ostatni == "Up"):
                Ostatni = "Up"
            else:
                Ostatni = "Down"

        if (Ostatni == "Left" and x1 > 20):
            x1 -= blok
        if (Ostatni == "Right" and x1 < 480 - width):
            x1 += blok
        if (Ostatni == "Up" and y1 > 20):
            y1 -= blok
        if (Ostatni == "Down" and y1 < 520 - height):
            y1 += blok

        display_surface.blit(text, textRect)
        # pygame.draw.rect(win, szary, (x, y, width, height))
        pygame.draw.rect(win, rozowy, (polex, poley, width, height))

        clock.tick(szybkosc)
        x1 += x1_change
        y1 += y1_change


        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_blocks.append(snake_Head)

        if len(snake_blocks) > snake_len:
            del snake_blocks[0]

        if (snake_Head in snake_blocks[:-1]):
            break

        our_snake(snake_block, snake_blocks)

        if (x1 == polex and y1 == poley):
            punkty += 1
            polex = random.randrange(20, 460, 20)
            poley = random.randrange(20, 460, 20)
            szybkosc *= 1.025
            snake_len += 1

        pygame.display.update()

        if (lastx == x1 and lasty == y1):
            print("Koniec Gry! Twój wynik to: " + str(punkty))
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
        print(punkty)
        # print("x:" + str(polex) + " y:" + str(poley))
        lastx = x1
        lasty = y1
    pygame.quit()

text_label = Label(root, font=40, text="Projket 1 - Paweł Kalisz")
text_label.pack()
click_button = Button(root, text="Obrazek", width=8, command=obrazek)
click_button.pack()
click_button = Button(root, text="Snake", width=8, command=gra)
click_button.pack()
click_button = Button(root, text="Beizer", width=8, command=beizer)
click_button.pack()

root.mainloop()
