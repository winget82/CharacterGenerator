import pygame, Settings, Armor, ArmorInstances, Character, Item, ItemInstances
import MapTiles, MonsterInstances, WeaponInstances, Weapons, sys
from pygame.locals import *


#set the character image and Rect
playerImage = Settings.player
playerRect = playerImage.get_rect()

def drawGame():
    #clear the surface
    surface.fill(Settings.colorBlack)

    #draw the map
    drawMap(newMap())

    #update the display
    pygame.display.flip()


def newMap():
    newMap = [[MapTiles.MapTiles(True, True, False, False, "Grass") for y in range(0,Settings.mapHeight)] for x in range(0,Settings.mapWidth)]

    newMap[0][0].tile = "Sand"
    newMap[10][10].tile = "Mountain"
    newMap[10][14].tile = "Mountain"
    newMap[10][12].tile = "Mountain"
    newMap[24][10].tile = "Mountain"
    newMap[9][18].tile = "Mountain"
    newMap[9][12].tile = "Mountain"
    newMap[24][18].tile = "Sand"

    return newMap


def drawMap(gameMap):

    for x in range(0,Settings.mapWidth):
        for y in range(0,Settings.mapHeight):
            if gameMap[x][y].tile == "Grass":
                surface.blit(Settings.grass, (x*Settings.cellWidth, y*Settings.cellHeight))
            elif gameMap[x][y].tile == "Sand":
                surface.blit(Settings.sand, (x*Settings.cellWidth, y*Settings.cellHeight))
            elif gameMap[x][y].tile == "Mountain":
                surface.blit(Settings.mountain, (x*Settings.cellWidth, y*Settings.cellHeight))


def gameLoop():
    gameQuit = False

    moveRight = False
    moveLeft = False
    moveUp = False
    moveDown = False

    playerRect.topleft = (Settings.screenWidth/2, Settings.screenHeight/2)

    while not gameQuit:

        #get player input
        eventsList = pygame.event.get()

        for event in eventsList:
            if event.type == pygame.QUIT:
                gameQuit = True
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                #Change the keyboard variables
                if event.key == K_LEFT or event.key == K_a:
                    moveRight = False
                    moveLeft = True
                if event.key == K_RIGHT or event.key == K_d:
                    moveLeft = False
                    moveRight =True
                if event.key == K_UP or event.key == K_w:
                    moveDown = False
                    moveUp = True
                if event.key == K_DOWN or event.key == K_s:
                    moveUp = False
                    moveDown = True
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_LEFT or event.key == K_a:
                    moveLeft = False
                if event.key == K_RIGHT or event.key == K_d:
                    moveRight = False
                if event.key == K_UP or event.key == K_w:
                    moveUp = False
                if event.key == K_DOWN or event.key == K_s:
                    moveDown = False

        #Move the player around
        #Move left
        if moveLeft and playerRect.left > 0:
            playerRect.move_ip(-1 * Settings.playerMoveRate, 0)
        #Move right
        if moveRight and playerRect.right < Settings.screenWidth:
            playerRect.move_ip(Settings.playerMoveRate, 0)
        #Move up
        if moveUp and playerRect.top > 0:
            playerRect.move_ip(0, -1 * Settings.playerMoveRate)
        #Move down
        if moveDown and playerRect.bottom < Settings.screenHeight:
            playerRect.move_ip(0, Settings.playerMoveRate)

        #Draw the window and game map
        drawGame()

        #Draw the playerRect to the surface of window
        surface.blit(playerImage, playerRect)
        #NEED TO SET THIS UP TO MOVE EXACTLY ONE TILE AT A TIME AND TO REPLACE THE TILE IMAGE WITH THE PLAYER RECT IMAGE

        pygame.display.update()

def gameInit():

    global surface, gameMap

    #initialize pygame
    pygame.init()

    #setup the window surface
    surface = pygame.display.set_mode((Settings.screenWidth, Settings.screenHeight))
    
    #window caption
    pygame.display.set_caption('Formidable Undertaking')

    gameMap = newMap()

if __name__ == '__main__':
    gameInit()
    gameLoop()