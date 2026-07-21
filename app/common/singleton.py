from abc import ABCMeta


class Singleton(ABCMeta):
	_instances = {}

	def __call__(cls, *args, **kawrgs):
		if cls not in cls._instances:
			instance = super().__call__(*args, **kawrgs)
			cls._instances[cls] = instance

		return cls._instances[cls]
