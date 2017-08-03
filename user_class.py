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
            print('Your symbols is wrong')
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
                print('You quantity of units is too big or too small, try again')
        return units

    def create_army(self):
        # User should be prompted to fill army line by line. (Depends on 'max_row' field)
        # User input should be like "aaw". (Depends on '_max_unit_in_a_row ' field)
        # we need to instantiating Army
        user_army = Army()
        count = 0
        self.display_info()
        while count != user_army._max_row:
            row = self.get_user_units(user_army)
            user_army._army.append(row)
            count += 1
        print(user_army._army)


def main():
    test_user = User()
    test_user.create_army()


if __name__ == '__main__':
    main()








