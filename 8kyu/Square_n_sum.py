"""
Complete the square sum function so that
it squares each number passed into it and then sums the results together.
"""


def square_sum(numbers):
	res = 0
	for num in numbers:
		res += num**2
	print (res)

square_sum ([1,2,3])











