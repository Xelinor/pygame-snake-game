import pygame
import Functions
from random import randint

class Tile(pygame.Rect):

    List = []
    width = 10
    height = 10
    total_tiles = 1
    H = 1
    V = 38
    Occupied = []
    Occupied_Numbers = []

    def __init__(self, x, y, Type):
        self.x = x
        self.y = y
        self.Type = Type
        self.number = Tile.total_tiles

        Tile.total_tiles += 1

        if Type == 'empty':
            self.walkable = True
        else:
            self.walkable = False

        pygame.Rect.__init__(self, (x, y), (Tile.width, Tile.height))
        Tile.List.append(self)

    @staticmethod
    def random_tile(start, end, exclude):
        valid = False

        while valid == False:
            test = randint(start, end)
            if test in exclude or test in Tile.Occupied_Numbers:
                continue
            else:
                valid = True

        for tile in Tile.List:
            if tile.number == test:
                return tile

    @staticmethod
    def get_tile(number):
        for tile in Tile.List:
            if tile.number == number:
                return tile

    @staticmethod
    def draw_tile(screen):
        for tile in Tile.List:
            if not (tile.Type == 'empty'):
                pygame.draw.rect(screen, (40, 40, 40), tile)

            #Functions.text_to_screen(screen, tile.number, tile.x, tile.y)

class Character(pygame.Rect):

    width = 10
    height = 10

    def __init__(self, x, y):
        pygame.Rect.__init__(self, x, y, Character.width, Character.height)
        
        self.x = x
        self.y = y

    def get_number(self):
        return ((self.x / self.width) + Tile.H) + ((self.y / self.height) * Tile.V)

    def get_tile(self):
        return Tile.get_tile(self.get_number())

class Body(Character):
    List = []
    total_segments = 0

    def __init__(self, x, y):
        Character.__init__(self, x, y)
        Body.List.append(self)
        self.number = Body.total_segments

        Body.total_segments += 1
        
        self.next_x = 0
        self.next_y = 0

    def motion(self, current_x, current_y):
        for segment in Body.List:

            if segment.number == 0:
                segment.x = current_x
                segment.y = current_y
            else:
                segment.x = segment.next_x
                segment.y = segment.next_y
                previous = segment.number - 1
                last_element = Body.List[previous]
                segment.next_x = last_element[0]
                segment.next_y = last_element[1]

    @staticmethod
    def draw(screen):
        for segment in Body.List:
            pygame.draw.rect(screen, (0,0,0), segment)

class Head(Character):
    List = []
    def __init__(self, x, y):
        Character.__init__(self, x, y)
        Head.List.append(self)

        self.velx = 0
        self.vely = 0

    def motion(self):
        current_x = self.x
        current_y = self.y
        direction = self.get_number() * self.vely
        if direction == 0:
            if self.velx > 0:
                future_tile = self.get_number() + Tile.H
            else:
                future_tile = self.get_number() - Tile.H
        else:
            if self.vely > 0:
                future_tile = self.get_number() + Tile.V
            else:
                future_tile = self.get_number() - Tile.V

        if Tile.get_tile(future_tile).walkable:
            self.x += self.velx
            self.y += self.vely
            Body.motion(self, current_x, current_y)
        else:
            self.velx = 0
            self.vely = 0

    @staticmethod
    def draw(screen):
        for head in Head.List:
            pygame.draw.rect(screen, (255,255,255), head)

class Apple(Character):
    List = []
    def __init__(self, x, y):
        Character.__init__(self, x, y)
        Apple.List.append(self)

    @staticmethod
    def draw(screen):
        for apple in Apple.List:
            pygame.draw.rect(screen, (0,0,0), apple, 6)