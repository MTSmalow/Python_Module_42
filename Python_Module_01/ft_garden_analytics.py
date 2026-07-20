#!/usr/bin/env python3

class Plant:
	class _Stats:
		def __init__(self):
			self.__grow_count = 0
			self.__age_count = 0
			self.__show_count = 0

		def record_grow(self):
			self.__grow_count = self.__grow_count + 1

		def record_age(self):
			self.__age_count = self.__age_count + 1

		def record_show(self):
			self.__show_count = self.__show_count + 1

		def display(self):
			print(f"Stats: {self.__grow_count} grow, {self.__age_count} age, {self.__show_count} show")

	def __init__(self, name: str, height: float, age: int, grow_rate: float):
		self._name = name
		self._height = height
		self._age = age
		self._grow_rate = grow_rate
		self._stats = self._Stats()

	@property
	def name(self):
		return self._name

	@property
	def stats(self):
		return self._stats

	@staticmethod
	def check_year_old(age: int) -> bool:
		return age > 365

	@classmethod
	def create_anonymous(cls):
		return cls("Unknown plant", 0.0, 0, 0.0)

	def show(self):
		print(f"{self._name}: {round(self._height, 1)}cm, {self._age} days old")
		self._stats.record_show()

	def age(self, days: int = 1):
		self._age = self._age + days
		self._stats.record_age()

	def grow(self):
		self._height = self._height + self._grow_rate
		self._stats.record_grow()

class Flower(Plant):
	def __init__(self, name: str, height: float, age: int, grow_rate: float, color: str):
		super().__init__(name, height, age, grow_rate)
		self.color = color
		self.is_blooming = False

	def bloom(self):
		self.is_blooming = True

	def grow(self):
		super().grow()
		self.bloom()

	def show(self):
		super().show()
		print(f"Color: {self.color}")
		if self.is_blooming:
			print(f"{self._name} is blooming beautifully!")
		else:
			print(f"{self._name} has not bloomed yet")

class Tree(Plant):
	class _TreeStats(Plant._Stats):
		def __init__(self):
			super().__init__()
			self.__shade_count = 0

		def record_shade(self):
			self.__shade_count = self.__shade_count + 1

		def display(self):
			super().display()
			print(f"{self.__shade_count} shade")

	def	__init__(self, name: str, height: float, age: int, grow_rate: float, trunk_diameter: float):
		super().__init__(name, height, age, grow_rate)
		self.trunk_diameter = trunk_diameter
		self._stats = self._TreeStats()

	def produce_shade(self):
		print(f"Tree {self._name} now produces a shade of {self._height}cm long and {self.trunk_diameter}cm wide.")
		self._stats.record_shade()

	def show(self):
		super().show()
		print(f"Trunk diameter: {self.trunk_diameter}cm")

class Vegetable(Plant):
	def __init__(self, name: str, height: float, age: int, grow_rate: float, harvest_seson: str):
		super().__init__(name, height, age, grow_rate)
		self.harvest_seson = harvest_seson
		self.notritional_value = 0

	def age(self, days: int = 1):
		super().age(days)
		self.notritional_value = self.notritional_value + 1

	def show(self):
		super().show()
		print(f"Harvest season: {self.harvest_seson}")
		print(f"Nutritional value: {self.notritional_value}")

class Seed(Flower):
	def __init__(self, name: str, height: float, age: int, grow_rate: float, color: str, seeds_per_bloom: int):
		super().__init__(name, height, age, grow_rate, color)
		self._seeds_per_bloom = seeds_per_bloom
		self.num_seeds = 0

	def bloom(self):
		super().bloom()
		self.num_seeds = self._seeds_per_bloom

	def show(self):
		super().show()
		print(f"Seeds: {self.num_seeds}")

def display_stats(plant: Plant):
	print(f"[statistics for {plant.name}]")
	plant.stats.display()

if __name__ == "__main__":
	print("=== Garden statistics ===")

	print("=== Check year-old")
	print(f"Is 30 days more than a year? -> {Plant.check_year_old(30)}")
	print(f"Is 400 days more than a year? -> {Plant.check_year_old(400)}")

	print("=== Flower")
	rose = Flower("Rose", 15.0, 10, 8.0, "red")
	rose.show()
	display_stats(rose)
	print("[asking the rose to grow and bloom]")
	rose.grow()
	rose.show()
	display_stats(rose)

	print("=== Tree")
	oak = Tree("Oak", 200.0, 365, 0.0, 5.0)
	oak.show()
	display_stats(oak)
	print("[asking the oak to produce shade]")
	oak.produce_shade()
	display_stats(oak)

	print("=== Seed")
	sunflower = Seed("Sunflower", 80.0, 45, 30.0, "yellow", 42)
	sunflower.show()
	print("[make sunflower grow, age and bloom]")
	sunflower.grow()
	sunflower.age(20)
	sunflower.show()
	display_stats(sunflower)

	print("=== Anonymous")
	unknown = Plant.create_anonymous()
	unknown.show()
	display_stats(unknown)