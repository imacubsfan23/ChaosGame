import pygame, random, os, sys, time
pygame.init()
pygame.display.set_caption('Chaos Game')
__author__ = 'Tim Dickeson II'

clock = pygame.time.Clock()
size = width, height = 1000, 1000
screen = pygame.display.set_mode(size)

white = (255,255,255)
red   = (255,0,0)
green = (0,255,0)
black = (0, 0, 0)

class Dot():
    def __init__(self, x, y, color):
        self.rect = pygame.Rect(3,3,3,3)
        self.rect.x = int(x)
        self.rect.y = int(y)
        self.color = color

def DrawWindow():
    screen.fill(black)

def getNumOfVertices():
    v = int(input("How many vertices do you want? "))
    return v if int(v) > 2 else getNumOfVertices()

def quit():
    pygame.quit()
    sys.exit()
    wait()

num_of_vertices = getNumOfVertices()
vertices = []
generated_dots = []
DrawWindow()

for vertex in range(num_of_vertices):
    print("{} {} left to place.".format(num_of_vertices, 'vertices' if num_of_vertices>1 else 'vertex'))
    vertex_placed = False
    while not vertex_placed:
        pygame.event.clear()
        event = pygame.event.wait()
        if event.type == pygame.QUIT: quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            v = Dot(event.pos[0], event.pos[1], red)
            vertices.append(v)
            pygame.draw.rect(screen, v.color, v.rect)
            num_of_vertices -= 1
            vertex_placed = True
    pygame.display.flip()

print("Click for Starting Point")
startpoint_placed = False
startpoint = None
while not startpoint_placed:
    pygame.event.clear()
    event = pygame.event.wait()
    if event.type == pygame.QUIT: quit()
    if event.type == pygame.MOUSEBUTTONDOWN:
        startpoint = Dot(event.pos[0], event.pos[1], white)
        pygame.draw.rect(screen, startpoint.color, startpoint.rect)
        startpoint_placed = True
pygame.display.flip()

lastpos = [startpoint.rect.x, startpoint.rect.y]
vval = len(vertices)-1 #useful vertices number
running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    random_vertex = vertices[random.randint(0, vval)]
    x = (random_vertex.rect.x + lastpos[0])/2
    y = (random_vertex.rect.y + lastpos[1])/2
    lastpos = (x,y)
    dot = Dot(x, y, white)
    pygame.draw.rect(screen, dot.color, dot.rect)

    pygame.display.flip()
