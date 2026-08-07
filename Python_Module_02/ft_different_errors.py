#!/usr/bin/env python3

def garden_operations(operation_number):
	if operation_number == 0:
		int("abc")
	if operation_number == 1:
		10 / 0
	if operation_number == 2:
		open("/non/existent/file")
	if operation_number == 3:
		"temperatura" + 10
	print("Operation completed successfully")


def test_error_types():
	print("=== Garden Error Types Demo ===")
	try:
		print("Testing operation 0...")
		garden_operations(0)
	except ValueError as e:
		print(f"Caught ValueError: {e}")

	try:
		print("Testing operation 1...")
		garden_operations(1)
	except ZeroDivisionError as e:
		print(f"Caught ZeroDivisionError: {e}")

	try:
		print("Testing operation 2...")
		garden_operations(2)
	except FileNotFoundError as e:
		print(f"Caught FileNotFoundError: {e}")

	try:
		print("Testing operation 3...")
		garden_operations(3)
	except TypeError as e:
		print(f"Caught TypeError: {e}")

	try:
		print("Testing operation 4...")
		garden_operations(4)
	except (TypeError, FileNotFoundError, ZeroDivisionError, ValueError) as e:
		print(e)

	print("All error types tested successfully!")