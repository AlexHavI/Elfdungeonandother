import pygame
from Constants import *

class Projective():
    def __init__(self,dir,image_pack):
        self.dir = dir
        self.image = pygame.image.load(image_pack).convert_alpha()
        self.image_pack = []
        self.image_pack.append(self.image.subsurface(0,0,64,64))
        self.image_pack.append(self.image.subsurface(64,0,64,64))
        self.image_pack.append(self.image.subsurface(128,0,64,64))
        self.image_pack.append(self.image.subsurface(192,0,64,64))

class Arrow(Projective):
    def __init__(self.dir):
        self.image = 'data/archerr.png'
        Projective.__init__(self, dir, self.image)
        
    
