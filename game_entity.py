from random import choice


class GameEntity():
    def __init__(self, staff, moneyStaffGame=0):
        super().__init__()
        self.__staff = staff
        self.__moneyStaff = moneyStaffGame

    @property
    def staff(self):
        return self.__staff

    def main_game(self):
            num_list = [n for n in range(1, 6)]
            win_num = 1 + choice(num_list)
            if self.__staff == win_num:
                print(f'You win, staff {win_num} win, your staff {self.staff}')
                return self.__moneyStaff * 2
            else:
                print(f'You lose,staff {win_num} win, Your staff {self.staff}')
                return self.__moneyStaff

    @property
    def moneyStaff(self):
        return self.__moneyStaff

