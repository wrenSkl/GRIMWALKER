import sdl2, sdl2.ext
from grimwalker._internal._globals import *

class Signal:
	def __init__(self, target_uid, signal_id):
		self._target_uid = target_uid
		self._signal_id = signal_id
		self._target = self.__get_target()

	def __get_target(self):
		if self._target_uid:
			return uids[self._target_uid]
		else:
			raise AttributeError("grimwalker.util.signal.Signal._target_uid does not exist or is an invalid type")

	@property
	def target_uid(self):
		return self._target_uid

	@target_uid.setter
	def target_uid(self, val):
		self._target_uid = val

	@property
	def signal_id(self):
		return self._signal_id

	@target_uid.setter
	def signal_id(self, val):
		self._signal_id = val
