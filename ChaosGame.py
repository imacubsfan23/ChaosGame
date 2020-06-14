import random
import pygame

all_dots = []
placed = []
pygame.init()
size = width, height = 600, 600
screen = pygame.display.set_mode(size)

white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
black = (0, 0, 0)
yellow = (255,255,0)
clock = pygame.time.Clock()
dots = int(input("How many dots do you want? "))
dotcount = dots
tdistance = 1/(dotcount-1)

def DrawWindow():
    screen.fill(black)

class Main():
    def __init__(self, x, y, color, id=10):
        self.rect = pygame.Rect(2, 2, 2, 2)
        self.rect.x = int(x)
        self.rect.y = int(y)
        self.id = dots
        self.color = color
        if self.id <= dots:
            all_dots.append(self)

for dot in range(dots):
    print("{} dots left to place.".format(dots))
    dot_placed = False
    while not dot_placed:
        pygame.event.clear()
        event = pygame.event.wait()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            Main(x, y, red, dots)
            dots -= 1
            dot_placed = True
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            wait()

print("Click for Starting Point")
startpoint = False
while not startpoint:
    pygame.event.clear()
    event = pygame.event.wait()
    if event.type == pygame.MOUSEBUTTONDOWN:
        startx, starty = event.pos
        Main(startx, starty, red, dots)
        startpoint = True
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
        wait()

simulating = True
lastpos = [startx, starty]
place = 100000
while simulating:
    choice = random.randint(1, dotcount)
    chosen = None
    for dot in all_dots:
        if dot.id == choice:
            chosen = dot

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            simulating = False

    if place > 0:
        x = (chosen.rect.x + int(lastpos[0]))*tdistance
        y = (chosen.rect.y + int(lastpos[1]))*tdistance
        Main(x, y, white)
        place -= 1

    lastpos[0] = x
    lastpos[1] = y

    for dot in all_dots:
        pygame.draw.rect(screen, (dot.color), dot.rect)
    for dot in placed:
        pygame.draw.rect(screen, (dot.color), dot.rect)

    pygame.display.flip()
    DrawWindow()
