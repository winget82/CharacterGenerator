import pygame

#Colors
colorBlack = (0,0,0)

#Screen size
screenWidth = 800
screenHeight = 600

#Map
mapWidth = 25
mapHeight = 19
cellWidth = 32
cellHeight = 32

#Fonts
# basicFont = pygame.font.SysFont(None, 24)

#Player movement
playerMoveRate = 16

#Sprites / Tiles
player = pygame.image.load("./NAFrpgTiles/Player.png")
grass = pygame.image.load("./NAFrpgTiles/Grass.png")
sand = pygame.image.load("./NAFrpgTiles/Sand.png")
mountain = pygame.image.load("./NAFrpgTiles/Mountain.png")