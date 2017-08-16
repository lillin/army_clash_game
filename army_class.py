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
        count = 0
        for i in self._army:
            for unit in i:
                if unit._status == True:
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

