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

    def print_army(self):
        # print user's army
        pass

    def is_alive(self):
        # get alive units quantity in created army
        pass

"""Create mechanism to retrieve user's input and transform it to army.

User should be prompted to fill army line by line. (Depends on 'max_row' field)

User input should be like "aawwmm". (Depends on '_max_unit_in_a_row ' field). 
This input should be validated. In case if it contains not only valid characters,
user should be asked to input this line one more time.

Create method in Army class to print army

Create method in Army class to get alive units quantity."""

