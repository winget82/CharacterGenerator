import pygame
import pytmx
from pytmx.util_pygame import load_pygame

pygame.init()

WindowX=800
WindowY=600

rect_color = (255, 0, 0)
poly_color = (0, 255, 0)
FPS=60

#Make pygame clock
clock = pygame.time.Clock()

screen=pygame.display.set_mode([WindowX,WindowY])

def render_tiles_to_screen(filename):
    tmx_data = load_pygame(filename)
    if tmx_data.background_color:
        screen.fill(pygame.Color(self.tmx_data.background_color))

    # iterate over all the visible layers, then draw them
    # according to the type of layer they are.
    for layer in tmx_data.visible_layers:

        # draw map tile layers
        if isinstance(layer, pytmx.TiledTileLayer):

            # iterate over the tiles in the layer
            for x, y, image in layer.tiles():
                screen.blit(image, (x * tmx_data.tilewidth, y * tmx_data.tileheight))

        # draw object layers
        elif isinstance(layer, pytmx.TiledObjectGroup):

            # iterate over all the objects in the layer
            for obj in layer:

                # objects with points are polygons or lines
                if hasattr(obj, 'points'):
                    pygame.draw.lines(screen, poly_color,
                            obj.closed, obj.points, 3)

                # some object have an image
                elif obj.image:
                    screen.blit(obj.image, (obj.x, obj.y))

                # draw a rect for everything else
                else:
                    pygame.draw.rect(screen, rect_color,
                            (obj.x, obj.y, obj.width, obj.height), 3)

        # draw image layers
        elif isinstance(layer, pytmx.TiledImageLayer):
            if layer.image:
                screen.blit(layer.image, (0, 0))

def main():
    running=True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running=False
        screen.fill((0,0,0))
        render_tiles_to_screen("./FUrpgTiles/FormidableUndertakingDungeon.tmx")
        pygame.display.flip()

main()

#Got this from:
# https://www.reddit.com/r/pygame/comments/2oxixc/pytmx_tiled/