#!/bin/python3
from math import sqrt, ceil, floor

class DivideDetermine:
	@staticmethod
	def main(n):
		print(1)
		print()
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
			
		print()
		print(n)
		


if __name__ == "__main__":
	DivideDetermine.main(int(eval(input("Enter integer of choice: "))))
