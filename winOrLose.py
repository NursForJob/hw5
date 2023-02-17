from game_entity import GameEntity
from decouple import config


class WinOrLose():
    def __init__(self):
        super().__init__()
        self.__money = int(config('MY_MONEY'))
        self.__staff = 0
        self.__moneyStaff = 0

    @property
    def money(self):
        return self.__money

    def start(self):
        game_of_end = False
        while not game_of_end:
            self.__staff = int(input('Введите ваш лот: '))
            self.__moneyStaff = int(input('Введите сумму ставки: '))
            game = GameEntity(self.__staff, self.__moneyStaff)
            if self.__moneyStaff == game.moneyStaff:
                self.__money -= self.__moneyStaff
                print(self.money)
            else:
                self.__money += self.__moneyStaff*2
                print(self.__money)
            print(game.main_game())
            if self.__money < 0:
                print('Игра окончена')
                game_of_end = True

