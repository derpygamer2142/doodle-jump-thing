import pygame, math
from Spritesheet import Spritesheet

class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        #3
        player_sheet = Spritesheet("spritesheet.png", 442, 3, 500, 45, 17, 21, (94, 129, 162))
        walk1 = player_sheet.get_image(1,0, 6, 3, 17*4, 21*4)
        walk2 = player_sheet.get_image(8,0, 6, 3, 17*4, 21*4)
        walk3 = player_sheet.get_image(9,0, 6, 3, 17*4, 21*4)
        walk4 = player_sheet.get_image(10,0, 6, 3, 17*4, 21*4)
        

        self.index = 0
        self.walkcycle = [walk1, walk2, walk3, walk4]
        self.image = self.walkcycle[self.index]
        self.rect = self.image.get_rect(center = (game.W_W/2,300))
        self.game = game
        self.rect.bottom = game.W_H/2
        self.yv = 0
        self.hit = False
        self.y = 0
        self.ignore = False
    def update(self):
        keys = pygame.key.get_pressed()

        self.rect.x += (int(keys[pygame.K_d])-int(keys[pygame.K_a]))*5
        # if pygame.sprite.spritecollide(self,self.game.tiles,False): self.ignore = True
        # else: self.ignore = False

        self.yv -= 1
        #self.rect.bottom -= self.yv
        self.y -= self.yv

        self.rect.bottom = self.y

        

        hits = pygame.sprite.spritecollide(self,self.game.tiles,False)
        actualHits = []
        for i in hits:
            if ((self.rect.bottom+self.yv) <= i.rect.top): actualHits.append(i)

        if len(actualHits) > 0 and self.yv < 0:
            self.rect.bottom += self.yv
            self.y = self.rect.bottom
            self.yv = 0
            if keys[pygame.K_w]:
                self.yv = 25.5
        
        if (self.y < self.game.W_H*0.25):
            self.game.camy += self.y - self.game.W_H*0.25
            self.y = self.game.W_H*0.25
        

        self.index += 0.1
        if self.index >= len(self.walkcycle):
            #print(f"wrapped at {self.index}")
            #print(len(self.walkcycle))
            self.index = 0
        #print(int(self.index))
        self.image = self.walkcycle[int(self.index)]
        # if pygame.sprite.spritecollide(self, self.game.enemy_sprite, False):
        #     self.hit = True
        #     print("bonk")

