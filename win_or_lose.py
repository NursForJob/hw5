from main import Main
from game import Game
from decouple import config


class Win_or_lose(Main):
    def __init__(self):
        super().__init__()
        self.__money = int(config('MY_MONEY'))
        self.__staff = 0

    def start(self):
        self.__staff = int(input('Введите вашу ставку'))
        game = Game(self.__staff)
        game.main_game()
