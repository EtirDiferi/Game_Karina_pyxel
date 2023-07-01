import pygame
from settings import *
from player import Player

#UWU

class Level:
    def __init__(self):
        # get the display surface
        self.display_surface = pygame.display.get_surface()

        #sprite groups
        self.all_sprites = pygame.sprite.Group()

        self.setup()

    def setup(self):
        self.player = Player(pos=(640,360), group=self.all_sprites)


    


    def run(self,dt):
        #print('run game')
        self.display_surface.fill('blue')
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(dt)