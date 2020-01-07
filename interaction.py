import pygame
import sys
from Classes import Tile
from Classes import Body

def interaction(screen, head):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                
                head.velx = 0
                head.vely = 0

                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    head.velx = 0
                    head.vely -= head.height

                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    head.velx = 0
                    head.vely += head.height

                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    head.velx -= head.width
                    head.vely = 0

                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    head.velx += head.width
                    head.vely = 0