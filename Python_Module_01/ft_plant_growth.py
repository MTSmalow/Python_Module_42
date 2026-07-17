#!/usr/bin/env python3

class Plant:
	def __init__(self, name: str, height: float, age: int, grow_rate:float):
		self.name = name
		self.height = height
		self.grow_old = age
		self.grow_rate = grow_rate


	def show(self):
		print(f"{self.name}: {round(self.height, 1)}cm, {self.grow_old} days old")

	def age(self):
		self.grow_old = self.grow_old + 1

	def grow(self):
		self.height = self.grow_rate + self.height

if __name__== "__main__":
	rose = Plant("Rose", 25.0, 30, 0.8)
	alt_init = rose.height
	print("=== Garden Plant Registry ===")
	rose.show()
	for i in range(1, 8):
		print(f"=== Day {i} ===")
		rose.grow()
		rose.age()
		rose.show()
	print(f"Growth this week: {round(rose.height-alt_init, 1)}")