from pygame import *
from config import *


class Platform(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.img = image.load("sprites/block.png")
        self.image = transform.scale(self.img, (BWIDTH, BHEIGHT))
        self.rect = Rect(x, y, BWIDTH, BHEIGHT)