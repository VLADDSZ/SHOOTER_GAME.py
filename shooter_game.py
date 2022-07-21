from pygame import *
from random import randint

class Prosto_sprayt(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, X, Y):
        super().__init__()
        self.X = X
        self.Y = Y
        self.image = transform.scale(image.load(player_image), (self.X, self.Y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



class gameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, X, Y):
        super().__init__()
        self.X = X
        self.Y = Y
        self.image = transform.scale(image.load(player_image), (self.X, self.Y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def fire(self):
        bullet = Bullet('bullet.png', player.rect.x + 35, player.rect.y + 50, -17, 40,90)
        bellets.add(bullet)
        self.image = transform.scale(image.load('Vlad2.png'), (self.X, self.Y))
    def Vlad1(self):
        self.image = transform.scale(image.load('Vlad1.png'), (self.X, self.Y))
    def Vlad3(self):
        self.image = transform.scale(image.load('Vlad3.png'), (self.X, self.Y))
    def Vlad4(self):
        self.image = transform.scale(image.load('Vlad4.png'), (self.X, self.Y))



    

class MONSTER(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, X,Y):
        super().__init__()
        self.X = X
        self.Y = Y
        self.image = transform.scale(image.load(player_image), (self.X, self.Y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y 
    def update(self):
        self.rect.y += Mspeed1
        if self.rect.y >= 800:
            self.rect.x = randint(5,460)
            self.rect.y = -100
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def UP(self):
        self.rect.y += -800
    def DOWN(self):
        self.rect.y += Mspeed1

Vlad = 'Vlad1.png'

class Bullet(gameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y <= -100:
            self.kill()

belety_count = 0
bellets = sprite.Group()

speed = 11
win_y = 500
win_x = 700
window = display.set_mode((win_y, win_x))

finish = False
Mspeed1 = 6

mixer.init()
shoot = mixer.Sound('byistryiy-perezaryad-obreza.ogg')
reloud = mixer.Sound('perezaryad-pistoleta.ogg')
minu_theme = mixer.Sound('prodoljitelnyiy-zvuk-kotoryiy-nagnetaet-situatsiyu-3003.ogg')
schelkane = mixer.Sound('schelkane-paltsem-34634.ogg')

font.init()
font2 = font.Font(None, 70)

reload_SPEED = 0
SHot_SPEED = 30
MAX_BELETY = 4



game = True
clock = time.Clock()
FPS = 60
q4 = 0
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

font.init()

monsters = sprite.Group()

player = gameSprite(Vlad, 5, win_x - 100,4,80,100)

DENGI = Prosto_sprayt('Dengi.png', 5, win_x - 300,4,70,70)

monster = MONSTER('monster4.png', randint(10,450),-130,110,110)

monsters.add(monster)

mixer.init()
mixer.music.load('2-06 Temporomandibular Grind.ogg')


q1 = 100
q2 = 0
DEAD_TIMER = 0
score = 0 
score2 = 0 
Slojnost = 0
Cost = 5

background = transform.scale(image.load('меню 1.png'), (win_y, win_x))
BG = 1
q3 = 0
q4 = 0 
game1 = True
while game1:
    for e in event.get():
        if e.type == QUIT:
            game = False
            game1 = False
    window.blit(background, (0,0))
    keys_presed = key.get_pressed()

    q4 -= 1
    if q4 == -1:
        minu_theme.play()
        q4 = 1100

    if keys_presed[K_UP] and BG == 2:
        background  = transform.scale(image.load('меню 1.png'), (win_y, win_x))
        BG = 1
        schelkane.play()
    if keys_presed[K_DOWN] and BG == 1:
        background  = transform.scale(image.load('меню 2.png'), (win_y, win_x))
        BG = 2
        schelkane.play()

    if keys_presed[K_UP] and BG == 4:
        background  = transform.scale(image.load('меню 3.png'), (win_y, win_x))
        BG = 3
        schelkane.play()
    if keys_presed[K_DOWN] and BG == 3:
        background  = transform.scale(image.load('меню 4.png'), (win_y, win_x))
        BG = 4
        schelkane.play()
    

    if keys_presed[K_RIGHT] and BG == 2:
        background  = transform.scale(image.load('меню 4.png'), (win_y, win_x))
        BG = 4
        schelkane.play()
        DEAD_TIMER = 1000
        Slojnost = 20
        Mspeed1 = 6.5
    if keys_presed[K_LEFT] and BG == 4:
        background  = transform.scale(image.load('меню 2.png'), (win_y, win_x))
        BG = 2
        schelkane.play()
        DEAD_TIMER = 0
        Slojnost = 0
        Mspeed1 = 6


    if keys_presed[K_RIGHT] and BG == 1:
        background  = transform.scale(image.load('тип обучение XD.png'), (win_y, win_x))
        schelkane.play()
    if keys_presed[K_RIGHT] and BG == 3:
        background  = transform.scale(image.load('тип обучение XD.png'), (win_y, win_x))
        schelkane.play()
    if keys_presed[K_LEFT] and BG == 1:
        background  = transform.scale(image.load('меню 1.png'), (win_y, win_x))
        schelkane.play()
    if keys_presed[K_LEFT] and BG == 3:
        background  = transform.scale(image.load('меню 3.png'), (win_y, win_x))
        schelkane.play()
    


    if keys_presed[K_SPACE]:
        game1 = False

    
    display.update()
    clock.tick(FPS)



background = transform.scale(image.load('fon_postal.png'), (win_y, win_x))
q4 = 0
mixer.music.play()



while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background, (0,0))
    q3 -= 1
    if q3 == -1:
        mixer.music.play()
        q3 = 10000
    if finish != True:

        if score2 >= Cost:
            DENGI.reset()
        DEAD_TIMER += 1
        if DEAD_TIMER == 1000:
            Mspeed1 += 0.1
            DEAD_TIMER = 0
            if Slojnost != 57:
                Slojnost += 1
        q2 += 1

        q1 += 1
        if q2 == 540 - Slojnost * 8:
            monster1 = MONSTER('monster4.png', randint(110,350),-330,300,300)
            monsters.add(monster1)
            q2 = 0
            if Slojnost != 57:
                Slojnost += 1
        if q2 == 70 - Slojnost:
            monster1 = MONSTER('monster1.png', randint(10,450),-230,randint(60,100),randint(60,100))
            monsters.add(monster1)
        if q2 == 140 - Slojnost * 2:
            monster1 = MONSTER('monster2.png', randint(10,450),-230,randint(60,100),randint(60,100))
            monsters.add(monster1)
        if q2 == 210 - Slojnost * 3:
            monster1 = MONSTER('monster2.png', randint(10,450),-230,randint(60,100),randint(60,100))
            monsters.add(monster1)
        if q2 == 280 - Slojnost * 4:
            monster1 = MONSTER('monster1.png', randint(10,450),-230,randint(60,100),randint(60,100))
            monsters.add(monster1)
        if q2 == 350 - Slojnost * 5:
            monster1 = MONSTER('monster3.png', randint(10,450),-230,randint(60,100),randint(60,100))
            monsters.add(monster1)
        if q2 == 420 - Slojnost * 6:
            monster1 = MONSTER('monster1.png', randint(10,450),-230,randint(60,100),randint(60,100))
            monsters.add(monster1)
        if q2 == 490 - Slojnost * 7:
            monster1 = MONSTER('monster3.png', randint(10,450),-230,randint(60,100),randint(60,100))
            monsters.add(monster1)



        
        bellets.update()
        bellets.draw(window)

        monsters.update()
        monsters.draw(window)

        player.reset()

        collides = sprite.groupcollide(monsters, bellets, True, True)
        for i in collides:
            score += 1
            score2 += 1 

        if sprite.spritecollide(player, monsters, False):
            finish = True


        if finish != True:
            keys_presed = key.get_pressed()
            if keys_presed[K_a] and player.rect.x > 5:
                player.rect.x -= speed
            if keys_presed[K_d] and player.rect.x < 420:
                player.rect.x += speed
            if keys_presed[K_w]:
                pass

            if keys_presed[K_b] and score2 >= Cost and SHot_SPEED != 5:
                SHot_SPEED -= 5
                Cost = Cost + 10
            if keys_presed[K_n] and score2 >= Cost and reload_SPEED != 40:
                reload_SPEED += 10
                Cost = Cost + 10
            if keys_presed[K_m] and score2 >= Cost and MAX_BELETY != 96:
                MAX_BELETY += 1
                Cost = Cost + 10

            
            if belety_count != MAX_BELETY:
                if q1 >= SHot_SPEED and keys_presed[K_w]:
                    belety_count +=1
                    q1 = 0
                    shoot.play()
                    player.fire()
                if q1 == 8:
                    player.Vlad1()
            else:
                if q1 == 1:
                    reloud.play()
                    player.Vlad3()
                if q1 == 41 - reload_SPEED:
                    player.Vlad4()
                if q1 == 70 - reload_SPEED:
                    player.Vlad1()
                if q1 == 80 - reload_SPEED:
                    belety_count = 0
    else:
        background = transform.scale(image.load('postal_FINAL.png'), (win_y, win_x))
        Final_text = font2.render(str(score), 1, (255, 0, 0))
        window.blit(Final_text, (340, 30))
        
        if q4 == 0:
            q4 = 1
            win_y = 500
            win_x = 500
            window = display.set_mode((win_y, win_x))
        
        
        

    display.update()
    clock.tick(FPS)
