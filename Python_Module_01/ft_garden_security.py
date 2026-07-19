#!/usr/bin/env python3

class Plant:
	def __init__(self, name: str, height: float, age: int):
		self._name = name
		self._height = height
		self._grow_old = age
		print(f"Plant created: {name}: {height}cm, {age} days old")


	def show(self):
		print(f"Current state: {self._name}: {round(self._height, 1)}cm, {self._grow_old} days old")

	def get_height(self):
		return self._height
	
	def get_age(self):
		return self._age
	
	def set_height(self, new_height: float ):
		if new_height < 0:
			print(f"{self._name}: Error, height can't be negative")
			print("Height update rejected")
		elif new_height >= 0:
			self._height = new_height
			print(f"Height updated: {new_height}cm")

	def set_age(self, new_age: float ):
		if new_age < 0:
			print(f"{self._name}: Error, age can't be negative")
			print("age update rejected")
		elif new_age >= 0:
			self._age = new_age
			print(f"age updated: {new_age}cm")

if __name__== "__main__":
	print("=== Garden Security System ===")
	rose = Plant("Rose", 15.0, 10)
	print("")
	rose.set_height(25.0)
	rose.set_age(30)
	print("")
	rose.set_height(-5)
	rose.set_age(-10)
	print("")
	rose.show()
