# calculations.py

def add(a, b):
	"""Compute and return the sum of two numbers.

	Usage examples:
	>>> add(4.0, 2.0)
	6.0
	>>> add(4, 2)
	6.0
	"""
	return float(a + b)

# python -m doctest calculations.py


def divide(a, b):
	"""Compute and return the quotient of two numbers.

	Usage examples:
	>>> divide(84, 2)
	42.0
	>>> divide(15, 3)
	5.0
	>>> divide(42, -2)
	-21.0

	>>> divide(42, 0)
	Traceback (most recent call last):
		File "<stdin>", line 1, in <module>
			divide(42, 0)
		File "<stdin>", line 2, in divide
			return float(a / b)
	ZeroDivisionError: division by zero
	"""
	return float(a / b)








