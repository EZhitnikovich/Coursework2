from platform import *
from random import choice, randint, shuffle
from bonusSpeedDown import BonusSpeedDown
from bonusSpeedUp import BonusSpeedUp


class LevelGenerator:

    @staticmethod
    def generateStartLevel(lineCount, entities, platforms, bonuses):
        startLevel = [[], [], [], [' ', ' ', ' ', ' ', '-', ' ', ' ', ' ', ' ']]

        while lineCount - 1:
            startLevel.insert(0, LevelGenerator.generateLinePattern(9))

            if not lineCount == 2:
                space = 3
            else:
                space = 2
            for i in range(space):
                startLevel.insert(0, [])

            lineCount -= 1

        y = 0

        for i in startLevel:
            if not i == []:
                LevelGenerator.generateObjects(i, y, entities, platforms, bonuses)
            y += BHEIGHT

    @staticmethod
    def generateLinePattern(length: int):
        allBlocks = [' ', '-']
        allBonuses = ['/', '+']
        line = []
        maxBlocks = 3
        maxBonuses = 1

        while len(line) != length:
            block = choice(allBlocks)
            if maxBlocks and block == "-":
                maxBlocks -= 1
                line.append(block)
            elif maxBonuses and randint(0, 100) == 25:
                line.append(choice(allBonuses))
                maxBonuses -= 1
            elif block != "-":
                line.append(block)

        if line.count('-') <= 2:
            line = LevelGenerator.generateLinePattern(length)

        shuffle(line)
        return line

    @staticmethod
    def generateNewRow(length, entities, platforms, bonuses):
        line = LevelGenerator.generateLinePattern(length)
        LevelGenerator.generateObjects(line, -BHEIGHT, entities, platforms, bonuses)

    @staticmethod
    def generateObjects(linePattern, y, entities, platforms, bonuses):
        x = 0
        for block in linePattern:
            if block == "-":
                pf = Platform(x, y)
                platforms.append(pf)
                entities.add(pf)
            elif block == "/":
                bonus = BonusSpeedDown(x, y)
                bonuses.append(bonus)
                entities.add(bonus)
            elif block == "+":
                bonus = BonusSpeedUp(x, y)
                bonuses.append(bonus)
                entities.add(bonus)
            x += BWIDTH
