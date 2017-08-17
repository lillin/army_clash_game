from unit_class import *


class Army:
    """Generic army class
    Army contains units and actually creating by user (belong to user)"""

    def __init__(self, _max_unit_in_a_row=3, _max_row=3):
        self._army = []
        self._max_unit_in_a_row = _max_unit_in_a_row
        self._max_row = _max_row

    def clash(self, army):
        # clash with other army
        # armies should fight line by line
        for row_index, row in enumerate(self._army):
            for col_index, unit in enumerate(row):
                unit.clash(army._army[row_index][col_index])
        return self.is_alive(), army.is_alive()

    def is_alive(self):
        # return qty of alive units
        count = 0
        for i in self._army:
            for unit in i:
                if unit.is_alive():
                    count += 1
        print('There are {qty} alive units in your army.'.format(qty=count))

    def print_army(self):
        # initially looks like this:
        # [['Warrior', 'Warrior', 'Warrior'], ['Archer', 'Archer', 'Archer'], ['Mage', 'Mage', 'Archer']]
        # output looks like this:
        # Warrior | Warrior | Warrior
        # Archer  | Archer  | Archer
        # Mage    | Mage    | Archer
        for i in self._army:
            print(' | '.join([x._type.ljust(len('warrior')) for x in i]))


def main():
    army_one = Army(2, 3)
    army_one._army = [[Warrior(), Warrior()], [Mage(), Mage()], [Archer(), Archer()]]
    army_two = Army(2, 3)
    army_two._army = [[Mage(), Archer()], [Warrior(), Warrior()], [Archer(), Mage()]]
    army_one.clash(army_two)


if __name__ == '__main__':
    main()
