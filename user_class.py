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

    def get_user_unit(self):
        # get units from user
        # return 1 unit
        valid = False
        while not valid:
            try:
                unit = input('Enter a letter: ')
                if unit in ('w', 'a', 'm'):
                    valid = True
                else:
                    print('Your value is not valid')
            except ValueError:
                print('Your value is not valid')
        return unit

    def create_row(self, user_army):
        # make 1 row getting unit from user
        row = ''
        while len(row) != user_army._max_unit_in_a_row:
            row += self.get_user_unit()
        print(row)
        return row

    def create_army(self):
        # User should be prompted to fill army line by line. (Depends on 'max_row' field)
        # User input should be like "aaw". (Depends on '_max_unit_in_a_row ' field)
        # we need to instantiating Army
        user_army = Army()
        count = 0
        self.display_info()
        while count != user_army._max_row:
            # create row
            row = self.create_row(user_army)
            user_army._army.append(row)
            count += 1
        print(user_army._army)

def main():
    test_user = User()
    test_user.create_army()


if __name__ == '__main__':
    main()








