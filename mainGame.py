import pygame
from player import Player
from platform import *
from levelGenerator import LevelGenerator


class MainGame:

    def __init__(self, winWidth: int, winHeight: int, hero: Player, windowName: str):
        self.winWidth = winWidth
        self.winHeight = winHeight
        self.display = (winWidth, winHeight)
        self.fallSpeed = 1
        pygame.init()
        self.screen = pygame.display.set_mode(self.display)
        pygame.display.set_caption(windowName)
        self.platforms = []
        self.bonuses = []
        self.entities = pygame.sprite.Group()
        self.hero = hero
        self.timer = pygame.time.Clock()
        self.gameStarted = False
        self.up = self.left = self.right = False

    def startGame(self):
        self.entities.add(self.hero)
        pic = pygame.image.load("sprites/background.png")
        pic = pygame.transform.scale(pic, self.display)

        level = LevelGenerator.generateLevelPattern(12, 9, True)

        LevelGenerator.platformStartLocation(level, self.entities, self.platforms, self.bonuses)

        startTick = pygame.time.get_ticks()
        lastSecond = 0

        run = True

        while run:
            if self.fallSpeed < 1:
                self.fallSpeed = 1
            if self.hero.moveSpeed < 2:
                self.hero.moveSpeed = 2
            seconds = (pygame.time.get_ticks() - startTick) / 1000
            pygame.display.set_caption(f"Go away, fps {round(self.timer.get_fps())}, {seconds}")
            if round(seconds) != lastSecond and self.gameStarted:
                self.fallSpeed += 0.0005
                self.hero.moveSpeed += 0.0005
                lastSecond += round(seconds)

            self.timer.tick(60)
            self.eventHandler()
            self.screen.blit(pic, (0, 0))
            self.hero.update(self.left, self.right, self.up, self.platforms)
            self.moveLocation()

            for b in self.bonuses:
                if sprite.collide_rect(self.hero, b):
                    self.hero.moveSpeed, self.fallSpeed = b.getBuff(self.hero.moveSpeed,
                                                                    self.fallSpeed)
                    b.remove(self.entities)
                    self.bonuses.remove(b)

            if self.hero.rect.y > self.winHeight:
                run = False

            pygame.display.update()

    def moveLocation(self):
        generate = True
        for e in self.entities:
            if isinstance(e, Platform) and e.rect.y > self.winHeight + BHEIGHT * 2:
                e.remove(self.entities)
                self.platforms.remove(e)
                if generate:
                    LevelGenerator.addLine(9, self.entities, self.platforms, self.bonuses)
                    generate = False

            if self.gameStarted:
                e.rect.y += self.fallSpeed
            self.screen.blit(e.image, e.rect.topleft)

    def eventHandler(self):
        for e in pygame.event.get():
            if e.type == QUIT:
                raise SystemExit("QUIT")
            if e.type == KEYDOWN and e.key == K_w:
                self.up = True
            if e.type == KEYDOWN and e.key == K_a:
                self.left = True
            if e.type == KEYDOWN and e.key == K_d:
                self.right = True
            if e.type == KEYDOWN:
                self.gameStarted = True

            if e.type == KEYUP and e.key == K_w:
                self.up = False
            if e.type == KEYUP and e.key == K_d:
                self.right = False
            if e.type == KEYUP and e.key == K_a:
                self.left = False
