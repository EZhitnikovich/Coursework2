from pygame import *
from config import *
import pyganim

animDelay = 120
stayAnim = ["sprites/character/stand/stand1.png",
            "sprites/character/stand/stand2.png",
            "sprites/character/stand/stand3.png",
            "sprites/character/stand/stand4.png"]

jumpAnim = ["sprites/character/jump/jump2.png"]

runAnim = ["sprites/character/run/run11.png",
           "sprites/character/run/run12.png",
           "sprites/character/run/run13.png",
           "sprites/character/run/run21.png",
           "sprites/character/run/run22.png",
           "sprites/character/run/run23.png"]


class Player(sprite.Sprite):
    width = 30
    height = 50

    def __init__(self, x: int, y: int):
        self.moveSpeed = 5
        self.jumpPower = 12
        self.gravity = 0.35
        sprite.Sprite.__init__(self)
        self.xVel = 0
        self.yVel = 0
        self.startX = x
        self.startY = y
        self.onGround = False
        self.image = image.load(stayAnim[0])
        self.image = transform.scale(self.image, (self.width, self.height))

        boltAnim = []
        for anim in stayAnim:
            img = image.load(anim)
            img = transform.scale(img, (self.width, self.height))
            boltAnim.append((img, animDelay))
        self.animStand = pyganim.PygAnimation(boltAnim)
        self.animStand.play()

        boltAnimRunRight = []
        boltAnimRunLeft = []
        for anim in runAnim:
            img = image.load(anim)
            img = transform.scale(img, (self.width, self.height))
            img2 = transform.flip(img, True, False)
            boltAnimRunRight.append((img, animDelay))
            boltAnimRunLeft.append((img2, animDelay))
        self.animRunRight = pyganim.PygAnimation(boltAnimRunRight)
        self.animRunRight.play()
        self.animRunLeft = pyganim.PygAnimation(boltAnimRunLeft)
        self.animRunLeft.play()

        boltAnimJumpRight = []
        boltAnimJumpLeft = []
        for anim in jumpAnim:
            img = image.load(anim)
            img = transform.scale(img, (self.width, self.height))
            img2 = transform.flip(img, True, False)
            boltAnimJumpLeft.append((img2, animDelay))
            boltAnimJumpRight.append((img, animDelay))
        self.animJumpLeft = pyganim.PygAnimation(boltAnimJumpLeft)
        self.animJumpLeft.play()
        self.animJumpRight = pyganim.PygAnimation(boltAnimJumpRight)
        self.animJumpRight.play()
        self.rect = Rect(x, y, self.width, self.height)

    def update(self, left: bool, right: bool, up: bool, platforms):

        if up:
            if self.onGround:
                self.yVel = -self.jumpPower

        if left:
            self.xVel = -self.moveSpeed
            self.image.fill(Color(0))
            if up:
                self.animJumpLeft.blit(self.image, (0, 0))
            else:
                self.animRunLeft.blit(self.image, (0, 0))

        if right:
            self.xVel = self.moveSpeed
            self.image.fill(Color(0))
            if up:
                self.animJumpRight.blit(self.image, (0, 0))
            else:
                self.animRunRight.blit(self.image, (0, 0))

        if not (left or right):
            self.xVel = 0
            if not up:
                self.image.fill(Color(0))
                self.animStand.blit(self.image, (0, 0))

        if not self.onGround:
            self.yVel += self.gravity

        if self.rect.x > WIN_WIDTH:
            self.rect.x = 0
        elif self.rect.x < 0:
            self.rect.x = WIN_WIDTH - self.width / 2

        self.onGround = False
        self.rect.y += self.yVel
        self.collide(0, self.yVel, platforms)

        self.rect.x += self.xVel
        self.collide(self.xVel, 0, platforms)

    def collide(self, xVel, yVel, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p):

                if xVel > 0:
                    self.rect.right = p.rect.left

                if xVel < 0:
                    self.rect.left = p.rect.right

                if yVel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yVel = 0

                if yVel < 0:
                    self.rect.top = p.rect.bottom
                    self.yVel = 0

    def resetStats(self):
        self.rect.x = self.startX
        self.rect.y = self.startY
        self.moveSpeed = 5
        self.yVel = 0
        self.xVel = 0
