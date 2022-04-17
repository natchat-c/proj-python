#Create your own shooter

from pygame import *
from random import randint

w = 700
h = 500

lost = 0
score = 0


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65,85))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x>10:
            self.rect.x -= 15
        if keys[K_RIGHT] and self.rect.x<630:
            self.rect.x += 15
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx-32, self.rect.top, 15)
        bullets.add(bullet)

class Enemy(GameSprite):
    def update(self):
        global lost
        self.rect.y += self.speed
        if self.rect.y > h:
            self.rect.y = 0
            self.rect.x = randint(0,w-80)
            lost  += 1
            

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()

enemys = sprite.Group()
for i in range(5):

    enemy = Enemy('ufo.png',randint(80,w-80),0,randint(1,4))
    enemys.add(enemy)

bullets = sprite.Group()
    

font.init()
font1 = font.SysFont('Arial',36)


window = display.set_mode((w,h)) 
display.set_caption("Shooter game")
background = transform.scale(image.load("galaxy.jpg"),(w,h))
mixer.init()
mixer.music.load('PhantomfromSpace.wav')
mixer.music.play()

shoot = mixer.Sound('fire.ogg')

player = Player("rocket.png",5,400,5)

clock = time.Clock()
FPS = 60
clock.tick(FPS)



Game = True

while Game:
    window.blit(background,(0,0))
    text = font1.render("Missed: "+str(lost),1,(255,255,255))
    point = font1.render("Scored: "+str(score),1,(255,255,255))
    win = font1.render("You Win!",1,(225,225,0))
    lose = font1.render("You Lose!",1,(225,0,0))
    window.blit(text,(5,5))
    window.blit(point,(5,30))  
    keys = key.get_pressed()

    if lost >= 3 or sprite.spritecollide(player,enemys,False):
        window.blit(lose,(w/2-50,h/2))
        Game = False

    spriteX = sprite.groupcollide(enemys,bullets, True, True)
    for c in spriteX:
        score += 1
        enemy = Enemy('ufo.png',randint(80,w-80),0,randint(1,4))
        enemys.add(enemy)

    if score >=10:
        window.blit(win,(w/2-50,h/2))
        Game = False
        


    for e in event.get():
        if e.type == QUIT:
            Game = False

        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                player.fire()
                shoot.play()
    
    bullets.update()
    bullets.draw(window)

    player.reset()
    player.update()

    enemys.update()
    enemys.draw(window)
    


    
    display.update()
    clock.tick(FPS)
    time.delay(30)
 