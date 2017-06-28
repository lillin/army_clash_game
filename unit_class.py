class Unit:
    """Generic unit class"""

    def __init__(self):
        self._hp = 2
        self._damage = 1
        self._type = 'Unit'

    def _clash(self, unit):
    	pass



class Warior(Unit):
	"""Child class of Unit class
	unit warior"""

	def __init__(self, arg):
		super().__init__()
		self.arg = arg

		

class Army:
	"""Generic army class"""

	def __init__(self, _max_unit_in_a_row=3, _max_row=3):
		self._army = []
		self._max_unit_in_a_row = _max_unit_in_a_row
		self._max_row = _max_row
