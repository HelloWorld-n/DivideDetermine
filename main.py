#!/bin/python3
from math import sqrt, ceil, floor
import ConsoleUtil

class DivideDetermine:
	@staticmethod
	def main(n):
		if n < 1:
			raise Exception(f"Excepted positive integer、 got {n} instead。")
		ConsoleUtil.applyForegroundColor(127, 127, 127)
		print(1)
		ConsoleUtil.applyForegroundColor(63, 63, 255)
		tm = []
		sroot = sqrt(n)
		for i in range(2, ceil(sroot)):
			if n % i == 0:
				print(i)
				tm = [i] + tm
		if floor(sroot) == ceil(sroot):
			print(floor(sroot))
		for i in tm:
			print(n // i)
		ConsoleUtil.applyForegroundColor(127, 127, 127)
		print(n)
		ConsoleUtil.applyDefaultColors()

while __name__ == "__main__":
	try:
		DivideDetermine.main(int(eval(input("Enter positive integer of choice: "))))
	except Exception as exception:
		ConsoleUtil.applyForegroundColor(255, 63, 63)
		print(exception)
		ConsoleUtil.applyDefaultColors()
