import pygame, sys
from settings import *
from level import Level
from debug import *

version = '1.2.2 uwu '

class Game:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
		pygame.display.set_caption(f'-- Kary_Pixel -- V{version}')
		self.clock = pygame.time.Clock()
		self.level = Level()
		

	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
  
			dt = self.clock.tick(100) / 1000
			self.level.run(dt)
			ddebug()

			pygame.display.update()

if __name__ == '__main__':
	game = Game()
	game.run()
