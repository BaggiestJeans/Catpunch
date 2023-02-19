import pygame
from pygame.locals import *
pygame.init()
SW=100
SH=100
screen=pygame.display.set_mode((SW,SH))                        
run=True
tile_size=0
block=pygame.image.load("Tile_Purple.png")
def draw_grid():
	for line in range(0, 6):
		pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (SW, line * tile_size))
		pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, SH))

class World():
	def __init__(self, data):
		self.tile_list = []

		block=pygame.image.load("Tile_Purple.png")

		row_count = 0
		for row in data:
			col_count = 0
			for tile in row:
				if tile == 1:
					img = pygame.transform.scale(block, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 2:
					img = pygame.transform.scale(block, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				col_count += 1
			row_count += 1

	def draw(self):
		for tile in self.tile_list:
			screen.blit(tile[0], tile[1])

# world = World(world_data)
while run:
    screen.fill((0,255,0))
    draw_grid()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    pygame.display.update()
pygame.quit()