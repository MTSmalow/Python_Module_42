#!/usr/bin/env python3

def input_temperature(temp_str):
	converted = int(temp_str)
	if converted < 0:
		raise Exception(f"{converted}°C is too cold for plants (min 0°C)")
	if converted > 40:
		raise Exception(f"{converted}°C is too hot for plants (max 40°C)")
	return converted

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
	
	try:
		print("Input data is '100'")
		input_temperature("100")
	except Exception as e:
		print(f"Caught input_temperature error: {e}\n")

	try:
		print("Input data is '-50'")
		input_temperature("-50")
	except Exception as e:
		print(f"Caught input_temperature error: {e}\n")

	print("All tests completed - program didn't crash!")

test_temperature()