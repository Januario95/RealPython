"""This module implements functions to process iterable."""

def find_value(value, iterable):
	"""Return True if value is in iterable, False otherwise."""
	# Be explicit by using iteration instead of membership
	for item in iterable:
		if value == item: # Find the element value by equality
			return True
	return False





