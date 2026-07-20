#!/usr/bin/env python3

class Plant:
	def __init__(self, name: str, height: float, age: int, grow_rate: float):
		self._name = name
		self._height = height
		self._age = age
		self._grow_rate = grow_rate

	def show(self):
		print(f"{self._name}: {round(self._height, 1)}cm, {self._age} days old")

	def age(self):
		self._age = self._age + 1

	def grow(self):
		self._height = self._height + self._grow_rate

class Flower(Plant):
	def __init__(self, name: str, height: float, age: int, grow_rate: float, color: str):
		super().__init__(name, height, age, grow_rate)
		self.color = color
		self.is_blooming = False

	def bloom(self):
		self.is_blooming = True

	def show(self):
		super().show()
		print(f"Color: {self.color}")
		if self.is_blooming:
			print(f"{self._name} is blooming beatfully!")
		else:
			print(f"{self._name} has not bloomed yet")

class Tree(Plant):
	def	__init__(self, name: str, height: float, age: int, grow_rate: float, trunk_diameter: float):
		super().__init__(name, height, age, grow_rate)
		self.trunk_diameter = trunk_diameter
	
	def produce_shade(self):
		print(f"Tree {self._name} now produces a shade of {self._height}cm long and {self.trunk_diameter}cm wide.")

	def show(self):
		super().show()
		print(f"Trunk diameter: {self.trunk_diameter}cm")

class Vegetable(Plant):
	def __init__(self, name: str, height: float, age: int, grow_rate: float, harvest_seson: str):
		super().__init__(name, height, age, grow_rate)
		self.harvest_seson = harvest_seson
		self.notritional_value = 0

	def age(self):
		super().age()
		self.notritional_value = self.notritional_value + 1

	def show(self):
		super().show()
		print(f"Harvest season: {self.harvest_seson}")
		print(f"Nutritional value: {self.notritional_value}")

if __name__ == "__main__":
	print("=== Garden Plant Types ===")

	print("=== Flower")
	rose = Flower("Rose", 15.0, 10, 0.8, "red")
	rose.show()
	print("[asking the rose to bloom]")
	rose.bloom()
	rose.show()

	print("=== Tree")
	oak = Tree("Oak", 200.0, 365, 5.0, 5.0)
	oak.show()
	print("[asking the oak to produce shade]")
	oak.produce_shade()

	print("=== Vegetable")
	tomato = Vegetable("Tomato", 5.0, 10, 2.1, "April")
	tomato.show()
	print("[make tomato grow and age for 20 days]")
	for _ in range(20):
			tomato.grow()
			tomato.age()
	tomato.show()