import sdl2, sdl2.ext

from grimwalker.type import EntityType

class Registry:
	def __init__(self, init_registry: dict = None, expected_datapoints = None):
		if init_registry:
			if type(init_registry) == dict:
				self._registry = init_registry
			else:
				raise TypeError("attempted to initialise grimwalker.util.registry.Registry but init_registry was of an unexpected type")
		if expected_datapoints:
			if type(expected_datapoints) == dict:
				self._expect = expected_datapoints
			else:
				raise TypeError("attempted to initialise grimwalker.util.registry.Registry but init_registry was of an unexpected type")
			
class EntityRegistry(Registry):
	def __init__(self, init_registry = None):
		super().__init__(self, init_registry, {
			"name": str,
			"type": EntityType,
			"further_data": dict
		})

entityReg = EntityRegistry()

__all__ = ["entityReg"]
