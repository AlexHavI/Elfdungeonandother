import pygame
from Constants import *
class Player():


    def __init__(self,name):

        self.state = ALIVE
        self.direction = RIGHT
        self.x = START_X
        self.y = START_Y
        self.name = name
        self.hp = MAX_HP
        self.mp = MAX_MP
        self.image_pack = ['data/archerr.png','data/archerd.png','data/archerl.png','data/archeru.png']
        self.images = []
        self.spell_casted = 0
        for image in self.image_pack:
            temp = pygame.image.load(image).convert_alpha()
            i = []
            i.append(temp.subsurface(0,0,64,64))
            i.append(temp.subsurface(64,0,64,64))
            i.append(temp.subsurface(128,0,64,64))
            self.images.append(i)

        self.mooving = [0,0,0,0]

    def moove(self):
        if self.mooving[RIGHT] == 5:
            self.direction = RIGHT
            self.x += PLAYER_SPEED
        if self.mooving[DOWN] == 5:
            self.direction = DOWN
            self.y += PLAYER_SPEED
        if self.mooving[LEFT] == 5:
            self.direction = LEFT
            self.x -= PLAYER_SPEED
        if self.mooving[UP] == 5:
            self.direction = UP
            self.y -= PLAYER_SPEED

        if self.x <= 0: self.x = 0
        if self.y <= 0: self.y = 0
        if self.x >= SCREEN_WIDTH - 60: self.x = SCREEN_WIDTH-60
        if self.y >= SCREEN_HEIGHT - 64: self.y = SCREEN_HEIGHT-64 

    
    def render(self,screen):
        screen.blit(self.images[self.direction][self.state], (self.x, self.y))
        
        
    def render_ui(self,screen):
        screen.blit(pygame.image.load('data/hpframe.png'),(self.x+12, self.y+58))
        screen.blit(pygame.image.load('data/mpframe.png'),(self.x+12, self.y+63))
        m = 1
        z = self.hp // 5
        while m <= z:
            screen.blit(pygame.image.load('data/hptick.png'),(self.x+11+m*2, self.y+ 59))
            m += 1
        m = 1
        z = self.mp // 5
        while m <= z:
            screen.blit(pygame.image.load('data/mptick.png'),(self.x+11+m*2, self.y+ 63))
            m += 1
    def die(self):
        self.hp = 0
        self.mp = 0
        self.state = DEAD

    def tick(self):
        if self.state != DEAD:
            self.mp += MP_REG
            self.hp += HP_REG
            if self.hp > MAX_HP:
                self.hp = MAX_HP
            if self.mp > MAX_MP:
                self.mp = MAX_MP
            if pygame.time.get_ticks() > self.spell_casted + 1000:
                self.state = ALIVE
            if self.hp <= 0:
                self.die()

