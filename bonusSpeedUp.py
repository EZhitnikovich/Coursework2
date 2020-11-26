from bonus import Bonus
from pygame import *


class BonusSpeedUp(Bonus):

    def __init__(self, x: int, y: int):
        self.img = image.load("sprites/su.png")
        super().__init__(x, y, self.img)

    def getBuff(self, fspeed, pspeed):
        return fspeed * 1.5, pspeed * 1.5
