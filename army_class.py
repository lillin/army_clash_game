from unit_class import *


class Army:
    """Generic army class
    Army contains units and actually creating by user (belong to user)"""

    def __init__(self, _max_unit_in_a_row=3, _max_row=3):
        self._army = []
        self._max_unit_in_a_row = _max_unit_in_a_row
        self._max_row = _max_row

    def clash(self):
        # clash with other army
        pass

    def is_alive(self):
        # get alive units quantity in created army
        pass

    def print_army(self):
        # initially looks like this:
        # [['Warrior', 'Warrior', 'Warrior'], ['Archer', 'Archer', 'Archer'], ['Mage', 'Mage', 'Archer']]
        # output looks like this:
        # Warrior | Warrior | Warrior
        # Archer  | Archer  | Archer
        # Mage    | Mage    | Archer
        for i in self._army:
            print(' | '.join([x._type.ljust(len('warrior')) for x in i]))
