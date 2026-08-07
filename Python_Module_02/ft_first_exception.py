#!/usr/bin/env python3

def input_temperature(temp_str):
	return int(temp_str)

def test_temperature():
	print("=== Garden Temperature ===\n")

	print("Input data is '25'")
	temperature = input_temperature("25")
	print(f"Temperature is now {temperature}°C\n")


	try:
		print("Input data is 'abc'")
		input_temperature("abc")
	except Exception as e:
		print(f"Caught input_temperature error: {e}\n")

	print("All tests completed - program didn't crash!")

test_temperature()