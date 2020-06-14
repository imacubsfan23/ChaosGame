import pygame, random, os, sys, time
pygame.init()
pygame.display.set_caption('Chaos Game')
__author__ = 'Tim Dickeson II'

clock = pygame.time.Clock()
size = width, height = 600, 600
screen = pygame.display.set_mode(size)

white = (255,255,255)
red = (255,0,0)
black = (0, 0, 0)

class Dot():
    def __init__(self, x, y, color, id=10):
        self.rect = pygame.Rect(3,3,3,3)
        self.rect.x = int(x)
        self.rect.y = int(y)
        self.id = dots
        self.color = color
        if self.id <= dots:
            all_dots.append(self)

def DrawWindow():
    screen.fill(black)

def getVertices():
    return int(input("How many vertices do you want? "))

def quit():
    pygame.quit()
    sys.exit()
    wait()

all_dots = []
placed = []
dots = getVertices()
dotcount = dots
tdistance = 1/(dotcount-1)

for dot in range(dots):
    print("{} {} left to place.".format(dots, 'vertices' if dots>1 else 'vertex'))
    dot_placed = False
    while not dot_placed:
        pygame.event.clear()
        event = pygame.event.wait()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            Dot(x, y, red, dots)
            dots -= 1
            dot_placed = True
        if event.type == pygame.QUIT: quit()

print("Click for Starting Point")
startpoint = False
while not startpoint:
    pygame.event.clear()
    event = pygame.event.wait()
    if event.type == pygame.MOUSEBUTTONDOWN:
        startx, starty = event.pos
        Dot(startx, starty, white, dots)
        startpoint = True
    if event.type == pygame.QUIT: quit()

running = True
lastpos = [startx, starty]
place = 100000
while running:
    choice = random.randint(1, dotcount)
    chosen = None
    for dot in all_dots:
        if dot.id == choice:
            chosen = dot
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    if place > 0:
        x = (chosen.rect.x + int(lastpos[0]))*tdistance
        y = (chosen.rect.y + int(lastpos[1]))*tdistance
        Dot(x, y, white)
        place -= 1

    lastpos[0] = x
    lastpos[1] = y

    for dot in all_dots:
        pygame.draw.rect(screen, (dot.color), dot.rect)
    for dot in placed:
        pygame.draw.rect(screen, (dot.color), dot.rect)

    pygame.display.flip()
    DrawWindow()
