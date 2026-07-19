#!/usr/bin/env python3

class Plant:
	def __init__(self, name: str, height: float, age: int, grow_rate:float):
		self.name = name
		self.height = height
		self.grow_old = age
		self.grow_rate = grow_rate


	def show(self):
		print(f"Created: {self.name}: {round(self.height, 1)}cm, {self.grow_old} days old")

	def age(self):
		self.grow_old = self.grow_old + 1

	def grow(self):
		self.height = self.grow_rate + self.height

if __name__== "__main__":
	print("=== Plant Factory Output ===")
	rose = Plant("Rose", 25.0, 30, 0.8)
	rose.show()
	oak = Plant("Oak", 200.0, 365, 0.8)
	oak.show()
	cactus = Plant("Cactus", 5.0, 90, 0.8)
	cactus.show()
	sunflower = Plant("Sunflower", 80.0, 45, 0.8)
	sunflower.show()
	fern = Plant("Fern", 15.0, 120, 0.8)
	fern.show()
