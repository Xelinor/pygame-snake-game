import pygame
import sys
from Functions import text_to_screen
from Tile_List import Big_Ass_List
from Classes import *
from interaction import interaction
from random import randint

pygame.init()
pygame.mixer.init()
pygame.font.init()

SCREENWIDTH = 380
SCREENHEIGHT = 900
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT), 0, 32)

Invalids = Big_Ass_List

for y in range(0, screen.get_height(),10):
    for x in range(0, screen.get_width(), 10):
        if Tile.total_tiles in Invalids:
            Tile(x, y, 'solid')
        else:
            Tile(x, y, 'empty')

clock = pygame.time.Clock()
fps = 1

first_apple = Tile.random_tile(958, 1588, Invalids)

head = Head(180, 400)
target = Apple(first_apple.x, first_apple.y)

#pygame.mixer.music.load("Music/BloodyTears.ogg")
#pygame.mixer.music.play(-1)

background = pygame.image.load("Images/Nokia_Phone.png")

while True:
    #Processes
    interaction(screen, head)
    #Processes
    #Logic
    head.motion()
    Tile.Occupied = []
    Tile.Occupied_Numbers = []
    for segment in Body.List:
        for tile in Tile.List:
            if tile.x == segment.x and tile.y == segment.y:
                Tile.Occupied.append(tile)
                Tile.Occupied_Numbers.append(tile.number)
            elif tile.number in Invalids:
                continue
            else:
                tile.Type = 'empty'
                tile.walkable = True
    for tile in Tile.Occupied:
        tile.Type = 'full'
        tile.walkable = False
    if target.x == head.x and target.y == head.y:
        Apple.List = []
        create_apple = Tile.random_tile(958, 1588, Invalids)
        Body(0,0)
        target = Apple(create_apple.x, create_apple.y)
        fps += 1
    #Logic
    #Draw
    screen.blit(background, (0,0))
    pygame.draw.rect(screen, (0,0,0), (68, 248, 233, 173), 2)
    Body.draw(screen)
    Head.draw(screen)
    Apple.draw(screen)
    pygame.display.flip()
    #Draw
    clock.tick(fps)