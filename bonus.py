from pygame import *
from config import *

class Bonus(sprite.Sprite):

    def __init__(self, x: int, y: int, img):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(img, (BWIDTH, BHEIGHT))
        self.rect = Rect(x, y, BWIDTH, BHEIGHT)

    def getBonus(self):
        pass
