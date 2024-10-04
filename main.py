import pygame, sys, random, time, math
from Player import Player
from Tile import Tile
#from tile_enum import TileEnum
from Timer import Timer

pygame.init()
W_W = 1280
W_H = 720
screen = pygame.display.set_mode((W_W,W_H))
pygame.display.set_caption("not doodle jump")
score = 0
startTime = time.time()

def gethigh():
    s = 0
    with open("scores.txt", "r") as file:
        for line in file:
            if (line != ""):
                s = max(float(line), s)
    return math.floor(s)

high = gethigh()

def grid(p,s): return round(p/s)*s

class Game():
    
    def __init__(self):
        self.W_W = W_W
        self.W_H = W_H
        self.camy = 0
        self.speed = 5
        self.BG_COLOR = (125, 125, 125)
        self.player_sprite = pygame.sprite.GroupSingle()
        self.player = Player(self)
        self.player_sprite.add(self.player)
        def uh(): pass
        self.spawntimer = Timer(1500,uh, True, True)

        self.tiles = pygame.sprite.Group()
        self.tiles.add(Tile(self,W_W/2,"grass",(W_H/2) + 40))
        print(grid(W_W/2 - 40,40),grid(340,40))
        for i in range(0,W_H+80,40):
            self.tiles.add(Tile(self,round(random.randint(0,W_W)/40)*40,"grass",i))
        self.font = pygame.font.Font(None, 74)
        
        
        
        #self.tile = Tile()


    def update(self):
        global score, high
        t = self.tiles.sprites()
        if (round(-score / t[len(t)-1].rect.height)*t[len(t)-1].rect.height < t[len(t)-1].baseheight):
            self.tiles.add(Tile(self,round(random.randint(0,W_W)/t[len(t)-1].rect.height)*t[len(t)-1].rect.height,"grass",round(-score / t[len(t)-1].rect.height)*t[len(t)-1].rect.height))
        self.player_sprite.update()
        self.tiles.update()
        self.spawntimer.update()
        self.spawntimer.duration = 1500 / max(((time.time() - startTime) / 20), 1)
        score = max(-self.camy, score)
        if (self.player.hit):
            self.spawntimer.stopTimer()
            self.player_sprite.remove(self.player)
            mx, my = pygame.mouse.get_pos()
            if ((mx > (W_W/2 - 100)) and (mx < (W_W/2 + 100)) and (my > (W_H/2 - 36.5)) and (my < (W_H/2 + 36.5)) and pygame.mouse.get_pressed()[0]):
                f = open("scores.txt", "a")
                f.write(str(score))
                f.write("\n")
                f.close()
                score = 0
                high = gethigh()
                self.__init__()

    
    def draw(self, screen):
        global score
        self.player_sprite.draw(screen)
        self.tiles.draw(screen)
        if (self.player.hit):
            text = self.font.render("Game Over", True, (128, 128, 128))
            text_rect = text.get_rect(center = (W_W / 2, W_H / 4))
            screen.blit(text, text_rect)
            text = self.font.render(f"Score: {(score):.2f}", True, (128, 128, 128))
            text_rect = text.get_rect(center = (W_W / 2, W_H / 3))
            screen.blit(text, text_rect)

            w = 200
            h = 75
            text_rect = pygame.rect.Rect(0, 0, w, h)
            text_rect.center = (W_W/2, W_H/2)
            pygame.draw.rect(screen, (100, 100, 100), text_rect)
            text = self.font.render("Restart", True, (188, 188, 188))
            text_rect = text.get_rect(center = (W_W / 2, W_H / 2))
            screen.blit(text, text_rect)
        else:
            text = self.font.render(f"Score: {(score):.2f}", True, (128, 128, 128))
            text_rect = text.get_rect(midleft = (W_W * (1/32), W_H * (1/16)))
            screen.blit(text, text_rect)
            text = self.font.render(f"High score: {high}", True, (128, 128, 128))
            text_rect = text.get_rect(midleft = (W_W * (1/32), W_H * (1/4)))
            screen.blit(text, text_rect)

        text = self.font.render(str(self.camy) + ", " + str(self.player.y), True, (188, 188, 188))
        text_rect = text.get_rect(center = (W_W / 2, W_H*0.8))
        screen.blit(text, text_rect)


game = Game()
clock = pygame.time.Clock()

# player_sprite = pygame.sprite.GroupSingle()
# player = Player()
# player_sprite.add(player)


bg_img = pygame.image.load("backgrounds.png")
bg_surf = pygame.Surface((bg_img.get_rect().width,bg_img.get_rect().height/3))
bg_surf.blit(bg_img,(0,0),(0,bg_img.get_rect().height/3,bg_img.get_rect().width,bg_img.get_rect().height/3))
bg_surf = pygame.transform.scale(bg_surf,(game.W_W,game.W_H))


running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

    screen.fill(game.BG_COLOR)
    screen.blit(bg_surf,(0,0))
    game.draw(screen)
    game.update()
    
    
    

    pygame.display.update()
    clock.tick(60)
pygame.quit()