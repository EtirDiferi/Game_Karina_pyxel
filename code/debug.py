import pygame
from player import *


#UWU

pygame.init()
font = pygame.font.Font(None,30)

def debug(info, y=10 ,x=10):
    display_surf = pygame.display.get_surface()
    debug_surf = font.render(str(info), True, 'white')
    debug_rect = debug_surf.get_rect(topleft = (x,y))
    pygame.draw.rect(display_surf,'black',debug_rect)
    display_surf.blit(debug_surf, debug_rect)



def ddebug():
    debug(pygame.mouse.get_pos())
    debug(pygame.mouse.get_pressed(), 40)
    debug('  Hey listen', pygame.mouse.get_pos()[1], pygame.mouse.get_pos()[0])
    