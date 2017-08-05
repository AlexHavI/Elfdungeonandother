# -*- coding: utf-8 -*-
import pygame
from Constants import *
from Player import *
from pygame.locals import *

class Main():
    def __init__(self,screen):
        self.screen = screen
        self.player = Player('Approx')
        self.background = pygame.image.load('data/background.jpg')
        self.running = True
        self.main_loop()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
                #peredvizhenie
            elif event.type == USEREVENT+1:
                self.player.tick()
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    self.player.mooving = [5,0,0,0]
                if event.key == K_DOWN:
                    self.player.mooving = [0,5,0,0]
                if event.key == K_LEFT:
                    self.player.mooving = [0,0,5,0]
                if event.key == K_UP:
                    self.player.mooving = [0,0,0,5]

                #Pri otzhimaniy klavish
            elif event.type == KEYUP:
                if event.key == K_UP:
                    self.player.mooving[UP] = 0
                if event.key == K_DOWN:
                    self.player.mooving[DOWN] = 0
                if event.key == K_RIGHT:
                    self.player.mooving[RIGHT] = 0
                if event.key == K_LEFT:
                    self.player.mooving[LEFT] = 0
                  #Drygie deistviya igroka
                if event.key == K_SPACE:
                    if self.player.state != DEAD:
                        self.player.die()
                    else:
                        self.player.state = ALIVE
                if event.key == K_z:
                    if self.player.mp >= SKILL1_COST and self.player.state != SHOOT:
                        self.player.mp -= SKILL1_COST
                        self.player.state = SHOOT
                        self.player.spell_casted = pygame.time.get_ticks()
                
    def render(self):
        #Prorisovka vsego-vsego

        self.screen.blit(self.background,(0,0))
        self.player.render(screen)
        self.player.render_ui(screen)
        pygame.display.flip()

    def main_loop(self):
        #Osnovnoy cukl programmi
       pygame.time.set_timer(USEREVENT+1, 100)
       while self.running == True:
            
            if self.player.state != DEAD:
                self.player.moove()
            self.render()
            self.handle_events()
            


screen= pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
game = Main(screen)
