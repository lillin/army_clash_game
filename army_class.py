from unit_class import *


class Army:
	"""Generic army class"""

	def __init__(self, _max_unit_in_a_row=3, _max_row=3):
		self._army = []
		self._max_unit_in_a_row = _max_unit_in_a_row
		self._max_row = _max_row