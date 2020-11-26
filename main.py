from player import Player
from config import *
from mainGame import MainGame

BACKGROUND_COLOR = "#004400"


def main():
    hero = Player(200 + Player.width/4, WIN_HEIGHT-BWIDTH-Player.width)
    game = MainGame(WIN_WIDTH, WIN_HEIGHT, hero, "Go away")
    game.startGame()


if __name__ == '__main__':
    main()
