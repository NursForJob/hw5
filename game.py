from random import choice
from win_or_lose import WinOrLose


class Game(WinOrLose):
    def __init__(self, staff):
        super().__init__()
        self.__staff = staff

    @property
    def staff(self):
        return self.__staff

    def main_game(self):
        num_list = [n for n in range(1, 6)]
        win_num = choice(num_list)
        print(win_num)
        print(self.staff)
        if self.__staff == win_num:
            return 'you win', self.__staff * 2  # todo return
        else:
            self.__staff -= self.__staff
            return 'You lose'   # todo return


game = Game(staff=5)
game.main_game()
