import sys


class Menu:
    """Menu class
    1 Player
    2 Players
    Configuration
    Exit
    """

    def __init__(self):
        self._options = {
            1: self.one_player_game,
            2: self.two_player_game,
            3: self.configurations,
            0: self.quite
        }

    def display_menu(self):
        print("""
        Please select an option
        
        1. One-player game
        2. Two-player game
        3. Configurations
        
        0. Quite
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

        # need noexit var to while loop for backing into previous menu after end activity
        # in selected option -- ???
        self.display_menu()
        choice = self.get_menu_choice()
        option = self._options.get(choice)
        option()


    def one_player_game(self):
        print('this is one-player game with computer')

    def two_player_game(self):
        print('this is the game with your friend')

    def configurations(self):
        pass

    def quite(self):
        # exit the game
        print('Goodbye!')
        sys.exit(0)


def main():
    menu_obj = Menu()
    menu_obj.manage_menu()


if __name__ == '__main__':
    main()
