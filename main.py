import pygame, Settings, Armor, ArmorInstances, Character, Item, ItemInstances
import MapTiles, MonsterInstances, WeaponInstances, Weapons


def drawGame():
    #clear the surface
    surface.fill(Settings.colorBlack)

    #draw the map
    drawMap(newMap())

    #draw the character


    #update the display
    pygame.display.flip()



def newMap():
    
    newMap = [[MapTiles.MapTiles(True, True, False, False, "Grass") for y in range(0,Settings.mapHeight)] for x in range(0,Settings.mapWidth)]

    newMap[5][5].tile = "Sand"
    newMap[10][10].tile = "Mountain"

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

    while not gameQuit:

        #get player input
        eventsList = pygame.event.get()

        for event in eventsList:
            if event.type == pygame.QUIT:
                gameQuit = True

        drawGame()

    pygame.quit()
    exit()


def gameInit():

    global surface, gameMap

    #initialize pygame
    pygame.init()

    surface = pygame.display.set_mode((Settings.screenWidth, Settings.screenHeight))

    gameMap = newMap()

if __name__ == '__main__':
    gameInit()
    gameLoop()