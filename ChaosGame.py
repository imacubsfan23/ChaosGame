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

all_dots = []
placed = []
dots = int(input("How many vertices do you want? "))
dotcount = dots
tdistance = 1/(dotcount-1)

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
def text_objects(text, font):
    textSurface = font.render(text, True, White)
    return textSurface, textSurface.get_rect()
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.Font('game_font.ttf',20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)
def quit():
    pygame.quit()
    sys.exit()
    wait()

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
