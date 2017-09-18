import sys
from user_class import *
from util_class import *
from army_class import *


class Menu:
    """Menu class
    """

    def __init__(self):
        self._options = {
            1: self.one_player_game,
            2: self.two_player_game,
            3: self.configurations,
            0: self.quit
        }

    def display_menu(self):
        print("""
Please select an option
        
1. One-player game
2. Two-player game
3. Configurations
        
0. Quit
        """)

    def get_menu_choice(self):
        valid = False
        while not valid:
            try:
                choice = int(input('Select option: '))
                if 0 <= choice <= 3:
                    valid = True
                else:
                    print('Your value is not valid, please try again')
            except ValueError:
                print('Your value is not valid, please try again')
        return choice

    def manage_menu(self):
        """Display & Correlate"""

        while True:
            self.display_menu()
            choice = self.get_menu_choice()
            option = self._options.get(choice)
            option()
            input('Press Enter to continue...')

    def one_player_game(self):
        army_one = User().create_army()
        army_two = Army()
        army_two._army = Util().generate_army(army_one._max_row, army_one._max_unit_in_a_row)
        print()
        print('Your army: ')
        army_one.print_army()
        print()
        print('Computer\'s army: ')
        army_two.print_army()
        print()
        army_one.clash(army_two)
        print()

    def two_player_game(self):
        army_one = User().create_army()
        army_two = User().create_army()
        print()
        print('User one army: ')
        army_one.print_army()
        print()
        print('User two army: ')
        army_two.print_army()
        print()
        print(army_one.clash(army_two))
        print()

    def configurations(self):
        # ability to save user army into .txt
        # ability to download saved army
        pass

    def quit(self):
        print('Goodbye!')
        sys.exit(0)


def main():
    menu_obj = Menu()
    menu_obj.manage_menu()


if __name__ == '__main__':
    main()
