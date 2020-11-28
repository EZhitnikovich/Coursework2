import pygame
from player import Player
from platform import *
from levelGenerator import LevelGenerator
import pygame_menu
from menuTheme import menuTheme


class MainGame:

    def __init__(self, winWidth: int, winHeight: int, hero: Player, windowName: str):
        self.gameStarted = False
        self.winWidth = winWidth
        self.winHeight = winHeight
        self.display = (winWidth, winHeight)
        self.bg = pygame.image.load("sprites/background.png")
        self.bg = pygame.transform.scale(self.bg, self.display)
        self.fallSpeed = 1
        pygame.init()
        self.bgsound = pygame.mixer.Sound("music/background.mp3")
        self.screen = pygame.display.set_mode(self.display)
        pygame.display.set_caption(windowName)
        self.platforms = []
        self.bonuses = []
        self.entities = pygame.sprite.Group()
        self.hero = hero
        self.timer = pygame.time.Clock()
        self.up = self.left = self.right = False

        self.menu = self.createMainMenu(winWidth, winHeight)

    def startGame(self):
        self.bgsound.set_volume(0.1)
        self.bgsound.play(-1)
        self.menu.mainloop(self.screen)

    def createMainMenu(self, w, h):
        menu = pygame_menu.Menu(h, w,
                                title="Main menu",
                                theme=menuTheme)
        menu.add_button('Start', self.mainLoop)
        menu.add_button('Exit', pygame_menu.events.EXIT)

        return menu

    def resetAll(self, entites: pygame.sprite.Group,
                 platfroms: list,
                 bonuses: list):
        for e in entites:
            e.remove(entites)

        platfroms.clear()
        bonuses.clear()
        self.up = self.left = self.right = False
        self.gameStarted = False
        self.fallSpeed = 1
        self.hero.resetStats()

    def mainLoop(self):
        self.resetAll(self.entities, self.platforms, self.bonuses)
        self.entities.add(self.hero)

        level = LevelGenerator.generateLevelPattern(12, 9, True)

        LevelGenerator.platformStartLocation(level, self.entities, self.platforms, self.bonuses)
        run = True

        startTick = 0
        lastSecond = 0

        while run:

            if not self.gameStarted:
                startTick = pygame.time.get_ticks()
                lastSecond = 0

            if self.fallSpeed < 1:
                self.fallSpeed = 1
            if self.hero.moveSpeed < 2:
                self.hero.moveSpeed = 2

            seconds = round((pygame.time.get_ticks() - startTick) / 1000)
            pygame.display.set_caption(f"Go away, fps {round(self.timer.get_fps())}")

            if seconds != lastSecond and self.gameStarted:
                self.fallSpeed += 0.0005
                self.hero.moveSpeed += 0.0005
                lastSecond += round(seconds)

            self.timer.tick(60)
            self.eventHandler()
            self.screen.blit(self.bg, (0, 0))
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

            self.screen.blit(pygame.font.SysFont("Comic sans ms", 14).render(f"Seconds {seconds}", True, (90, 52, 145)),
                                                (0, 0))
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
