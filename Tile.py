import pygame, math, random
from Spritesheet import Spritesheet


class Tile(pygame.sprite.Sprite):
    def __init__(self,game, x, type, baseheight):
        super().__init__()
        self.type = type
        self.game = game
        self.tile_sheet = Spritesheet("spritesheet.png", 3, 3, 21*6 + 10, 21*12 + 24, 21, 21, (93, 129, 162))
        #self.tile_sheet = pygame.transform.scale(self.tile_sheet, (300, 600))
        
        tile1 = self.tile_sheet.get_image(self.get_type()[0],self.get_type()[1], 2, 2, 40, 40)
        self.image = tile1
        
        #self.image = self.tile_sheet
        self.rect = self.image.get_rect(center=(300, 400))
        self.rect.top = self.game.W_H/2
        self.y = baseheight#round((random.randint(0,self.game.W_H) + baseheight) / self.rect.height) * self.rect.height#self.game.W_H/2
        self.rect.left = x
        self.baseheight = baseheight
    def update(self):
        #if (not self.game.player.hit):
            #self.rect.left -= self.game.speed
        #if (self.rect.right < 0):
            #self.rect.left = self.game.W_W
        self.rect.top = self.y - self.game.camy

    def draw(self):
        self.image = self.tile_sheet
    
    def get_type(self):
        x, y = 0, 0
        '''if self.type == TileEnum.GRASS:
            x, y = 3, 4
        if self.type == TileEnum.DIRT:
            x, y = 3, 0
        if self.type == TileEnum.PURPLE:
            x, y = 3, 6
        if self.type == TileEnum.SNOW:
            x, y = 3, 2
        '''
        x,y = 3,4
        
        
        return (x, y)
