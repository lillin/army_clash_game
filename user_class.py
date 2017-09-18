from army_class import *


class User:
    """Generic user class
    Allows to create army"""

    def __init__(self):
        self._name = 'User'

    def display_info(self):
        # print info for user about allowed units
        print('Welcome to army constructor!')
        print()
        print('Enter w to add Warrior')
        print('Enter a to add Archer')
        print('Enter m to add Mage')

    def unit_validator(self, units):
        try:
            if all(i in 'wam' for i in units):
                return True
            else:
                print('Your letter not w or a or m')
                return False
        except ValueError:
            print('Your symbols are wrong')
            return False

    def get_user_units(self, user_army):
        # get full row with len == _max_units_in_the_row
        units_in_row = user_army._max_unit_in_a_row
        valid = False
        while not valid:
            units = input('Enter you {0} letters: '.format(units_in_row))
            print(units)
            if len(units) == units_in_row:
                valid = self.unit_validator(units)
            else:
                print('Your quantity of units is too big or too small, try again')
        return units

    def instantiating_unit(self, row):
        units_list = []
        for i in row:
            if i == 'w':
                units_list.append(Warrior())
            elif i == 'a':
                units_list.append(Archer())
            elif i == 'm':
                units_list.append(Mage())
        return units_list

    def create_army(self):
        user_army = Army()
        count = 0
        self.display_info()
        while count != user_army._max_row:
            row = self.get_user_units(user_army)
            user_army._army.append(self.instantiating_unit(row))
            count += 1
        return user_army


def main():
    test_user = User()
    test_user.create_army().is_alive()


if __name__ == '__main__':
    main()








