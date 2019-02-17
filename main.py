#Imports
import pygame, Settings, Armor, ArmorInstances, Character, Item, ItemInstances
import MapTiles, MonsterInstances, WeaponInstances, Weapons, sys, pytmx
from pygame.locals import *
from pytmx.util_pygame import load_pygame

#Initiate pygame
pygame.init()

rect_color = (255, 0, 0)
poly_color = (0, 255, 0)

#Set frames per second
FPS=60

#Make pygame clock
clock = pygame.time.Clock()

#Make the game window surface
surface = pygame.display.set_mode((Settings.screenWidth, Settings.screenHeight))

#Caption the game window
pygame.display.set_caption('Formidable Undertaking')


def renderTiles(filename):
    tmx_data = load_pygame(filename)
    if tmx_data.background_color:
        surface.fill(pygame.Color(self.tmx_data.background_color))

    # iterate over all the visible layers, then draw them according to the type of layer they are.
    for layer in tmx_data.visible_layers:

        # draw map tile layers
        if isinstance(layer, pytmx.TiledTileLayer):

            # iterate over the tiles in the layer
            for x, y, image in layer.tiles():
                surface.blit(image, (x * tmx_data.tilewidth, y * tmx_data.tileheight))

        # draw object layers
        elif isinstance(layer, pytmx.TiledObjectGroup):

            # iterate over all the objects in the layer
            for obj in layer:

                # objects with points are polygons or lines
                if hasattr(obj, 'points'):
                    pygame.draw.lines(surface, poly_color,
                            obj.closed, obj.points, 3)

                # some object have an image
                elif obj.image:
                    surface.blit(obj.image, (obj.x, obj.y))

                # draw a rect for everything else
                else:
                    pygame.draw.rect(surface, rect_color,
                            (obj.x, obj.y, obj.width, obj.height), 3)

        # draw image layers
        elif isinstance(layer, pytmx.TiledImageLayer):
            if layer.image:
                surface.blit(layer.image, (0, 0))


#set the initial character image and Rect
playerImage = pygame.transform.scale(Settings.player, (24,24))
playerRect = playerImage.get_rect()

animationFrameR = 0
animationFrameL = 0
animationFrameU = 0
animationFrameD = 0

spriteListR = [pygame.image.load('./FUCharacterArt/Nerk/Nerk_Walk/tile_28.png'),
                pygame.image.load('./FUCharacterArt/Nerk/Nerk_Walk/tile_29.png'),
                pygame.image.load('./FUCharacterArt/Nerk/Nerk_Walk/tile_30.png'),
                pygame.image.load('./FUCharacterArt/Nerk/Nerk_Walk/tile_31.png'),
                pygame.image.load('./FUCharacterArt/Nerk/Nerk_Walk/tile_32.png'),
                pygame.image.load('./FUCharacterArt/Nerk/Nerk_Walk/tile_33.png'),
                pygame.image.load('./FUCharacterArt/Nerk/Nerk_Walk/tile_34.png'),
                pygame.image.load('./FUCharacterArt/Nerk/Nerk_Walk/tile_35.png')]
spriteListL = [pygame.image.load('./FUCharacterArt/Nerk/Nerk_Walk/tile_10.png'),
                pygame.image.load('./FUCharacterArt/Nerk/Nerk_Walk/tile_11.png'),
                pygame.image.load('./FUCharacterArt/Nerk/Nerk_Walk/tile_12.png'),
                pygame.image.load('./FUCharacterArt/Nerk/Nerk_Walk/tile_13.png'),
                pygame.image.load('./FUCharacterArt/Nerk/Nerk_Walk/tile_14.png'),
                pygame.image.load('./FUCharacterArt/Nerk/Nerk_Walk/tile_15.png'),
                pygame.image.load('./FUCharacterArt/Nerk/Nerk_Walk/tile_16.png'),
                pygame.image.load('./FUCharacterArt/Nerk/Nerk_Walk/tile_17.png')]
spriteListU = [pygame.image.load('./FUCharacterArt/Nerk/Nerk_Walk/tile_01.png'),
                pygame.image.load('./FUCharacterArt/Nerk/Nerk_Walk/tile_02.png'),
                pygame.image.load('./FUCharacterArt/Nerk/Nerk_Walk/tile_03.png'),
                pygame.image.load('./FUCharacterArt/Nerk/Nerk_Walk/tile_04.png'),
                pygame.image.load('./FUCharacterArt/Nerk/Nerk_Walk/tile_05.png'),
                pygame.image.load('./FUCharacterArt/Nerk/Nerk_Walk/tile_06.png'),
                pygame.image.load('./FUCharacterArt/Nerk/Nerk_Walk/tile_07.png'),
                pygame.image.load('./FUCharacterArt/Nerk/Nerk_Walk/tile_08.png')]
spriteListD = [pygame.image.load('./FUCharacterArt/Nerk/Nerk_Walk/tile_19.png'),
                pygame.image.load('./FUCharacterArt/Nerk/Nerk_Walk/tile_20.png'),
                pygame.image.load('./FUCharacterArt/Nerk/Nerk_Walk/tile_21.png'),
                pygame.image.load('./FUCharacterArt/Nerk/Nerk_Walk/tile_22.png'),
                pygame.image.load('./FUCharacterArt/Nerk/Nerk_Walk/tile_23.png'),
                pygame.image.load('./FUCharacterArt/Nerk/Nerk_Walk/tile_24.png'),
                pygame.image.load('./FUCharacterArt/Nerk/Nerk_Walk/tile_25.png'),
                pygame.image.load('./FUCharacterArt/Nerk/Nerk_Walk/tile_26.png')]
animationFrameR = (animationFrameR + 1)# % len(spriteListR)
animationFrameL = (animationFrameL + 1)# % len(spriteListL)
animationFrameU = (animationFrameU + 1)# % len(spriteListU)
animationFrameD = (animationFrameD + 1)# % len(spriteListD)

def gameLoop():

    gameQuit = False
    moveRight = False
    moveLeft = False
    moveUp = False
    moveDown = False

    #starting position of player
    playerRect.topleft = (Settings.screenWidth/2, Settings.screenHeight*.925)

    while not gameQuit:

        #Frames per second
        clock.tick(FPS)

        playerImage = pygame.transform.scale(Settings.player, (24,24))
        surface.blit(playerImage, playerRect)

        #Get player input (events)
        eventsList = pygame.event.get()

        for event in eventsList:
            if event.type == pygame.QUIT:
                gameQuit = True
                pygame.quit()
                sys.exit()

            #Keydown events
            if event.type == KEYDOWN:
                #Change the keyboard variables
                if event.key == K_LEFT or event.key == K_a:
                    moveRight = False
                    moveLeft = True
                    Settings.player = spriteListL[animationFrameL]

                if event.key == K_RIGHT or event.key == K_d:
                    moveLeft = False
                    moveRight =True
                    Settings.player = spriteListR[animationFrameR]

                if event.key == K_UP or event.key == K_w:
                    moveDown = False
                    moveUp = True
                    Settings.player = spriteListU[animationFrameU]

                if event.key == K_DOWN or event.key == K_s:
                    moveUp = False
                    moveDown = True
                    Settings.player = spriteListD[animationFrameD]


            #Keyup events
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_LEFT or event.key == K_a:
                    moveLeft = False
                    # set character image to one facing left
                    Settings.player = pygame.image.load('./FUCharacterArt/Nerk/Nerk_Walk/tile_09.png')
                if event.key == K_RIGHT or event.key == K_d:
                    moveRight = False
                    # set character image to one facing right
                    Settings.player = pygame.image.load('./FUCharacterArt/Nerk/Nerk_Walk/tile_27.png')
                if event.key == K_UP or event.key == K_w:
                    moveUp = False
                    # set character image to one facing up
                    Settings.player = pygame.image.load('./FUCharacterArt/Nerk/Nerk_Walk/tile_00.png')
                if event.key == K_DOWN or event.key == K_s:
                    moveDown = False
                    # set character image to one facing down
                    Settings.player = pygame.image.load('./FUCharacterArt/Nerk/Nerk_Walk/tile_18.png')
        #Move the player
        #Move left
        if moveLeft and playerRect.left > 0:
            playerRect.move_ip(-1 * Settings.playerMoveRate, 0)
            # load list of 3 character tiles
            # set to one of the indices then cycle through them
            playerImage = spriteListL[animationFrameL]
            
        #Move right
        if moveRight and playerRect.right < Settings.screenWidth:
            playerRect.move_ip(Settings.playerMoveRate, 0)
            # load list of 3 character tiles
            # set to one of the indices then cycle through them
            playerImage = spriteListR[animationFrameR]
            
        #Move up
        if moveUp and playerRect.top > 0:
            playerRect.move_ip(0, -1 * Settings.playerMoveRate)
            # load list of 3 character tiles
            # set to one of the indices then cycle through them
            playerImage = spriteListU[animationFrameU]
            
        #Move down
        if moveDown and playerRect.bottom < Settings.screenHeight:
            playerRect.move_ip(0, Settings.playerMoveRate)
            # load list of 3 character tiles
            # set to one of the indices then cycle through them
            playerImage = spriteListD[animationFrameD]
            
        #Update portions of the screen
        pygame.display.update()
        
        #surface.fill((0,0,0))

        #render .tmx map file made with Tiled and map tile set by NEED TO CREDIT THE ARTIST HERE
        renderTiles(Settings.tileMap)
        
        #Update the display surface to screen
        pygame.display.flip()


if __name__ == '__main__':
    gameLoop()