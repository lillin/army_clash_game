import random
from army_class import *


class Util:

    def generate_army(self, max_row, max_units_in_a_row):
        return [[random.choice([Warrior(), Archer(), Mage()]) for _ in range(max_units_in_a_row)] for _ in range(max_row)]


def main():
    test_army = Army(3, 5)
    test_army._army = Util().generate_army(5, 3)
    test_army.print_army()


if __name__ == '__main__':
    main()
