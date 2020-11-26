from platform import *
from random import choice, randint
from bonusSpeedDown import BonusSpeedDown
from bonusSpeedUp import BonusSpeedUp


class LevelGenerator:

    @staticmethod
    def generateLinePattern(length: int):

        allBlocks = [' ', '-']
        allBonuses = ['/', '+']

        string = ""
        maxBlocks = 3
        maxBonuses = 1

        for i in range(length):
            block = choice(allBlocks)
            if maxBlocks > 0 and block == "-":
                string += block
                maxBlocks -= 1
            elif block != '-':
                string += block

            if maxBonuses > 0 and randint(0, 100) == 25:
                string += choice(allBonuses)
                maxBonuses -= 1

        if string.count("-") <= 2:
            string = LevelGenerator.generateLinePattern(length)

        print(string)
        return string

    @staticmethod
    def generateLevelPattern(count: int, length: int, isStart: bool):
        if isStart:
            level = ["    -    "]
        else:
            level = []

        while count:
            if len(level) % 4 == 0:
                level.insert(0, LevelGenerator.generateLinePattern(length))
            else:
                level.insert(0, "         ")
            count -= 1

        return level

    @staticmethod
    def addLine(length: int, entities, platforms, bonuses):
        line = LevelGenerator.generateLinePattern(length)
        x = 0
        for ch in line:
            if ch == "-":
                pf = Platform(x, -BHEIGHT)
                platforms.append(pf)
                entities.add(pf)
            elif ch == "/":
                bonus = BonusSpeedDown(x, -BHEIGHT)
                bonuses.append(bonus)
                entities.add(bonus)
            elif ch == "+":
                bonus = BonusSpeedUp(x, -BHEIGHT)
                bonuses.append(bonus)
                entities.add(bonus)
            x += BWIDTH

    @staticmethod
    def platformStartLocation(levelPattern, entities, platforms, bonuses):
        x = y = 0
        for row in levelPattern:
            for ch in row:
                if ch == "-":
                    pf = Platform(x, y)
                    entities.add(pf)
                    platforms.append(pf)
                elif ch == "/":
                    bonus = BonusSpeedDown(x, -y)
                    bonuses.append(bonus)
                    entities.add(bonus)
                elif ch == "+":
                    bonus = BonusSpeedUp(x, -y)
                    bonuses.append(bonus)
                    entities.add(bonus)
                x += BWIDTH
            y += BHEIGHT
            x = 0
