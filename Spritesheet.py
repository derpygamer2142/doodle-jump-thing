import pygame

class Spritesheet():
    def __init__(self, imgSource, x, y, w, h, spritewidth, spriteheight, colorkey):
        self.spritesheet = pygame.image.load(imgSource)
        self.surface = pygame.Surface((w, h))
        self.surface.blit(self.spritesheet,(0, 0), (x, y, w, h))
        self.spritewidth = spritewidth
        self.spriteheight = spriteheight
        # self.surface.set_colorkey(colorkey)
        self.colorkey = colorkey
    
    def get_image(self, texCoordX, texCoordY, offX, offY, scaledW, scaledH):
        sub_surf = pygame.Surface((self.spritewidth, self.spriteheight)).convert_alpha()
        sub_surf.blit(self.surface, (0, 0), ((texCoordX*self.spritewidth) + (texCoordX*offX), (texCoordY*self.spriteheight) + (texCoordY*offY), self.spritewidth, self.spriteheight))
        sub_surf = pygame.transform.scale(sub_surf, (scaledW, scaledH))
        sub_surf.set_colorkey(self.colorkey)
        return sub_surf