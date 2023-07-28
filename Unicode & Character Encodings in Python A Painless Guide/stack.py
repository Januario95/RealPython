
class Stack:
	def __init__(self):
		self.stack = []

	def is_empty(self):
		return self.stack == []

	def push(self, item):
		self.stack.append(item)

	def pop(self):
		if self.is_empty():
			return 'Stack is empty'

		return self.stack.pop()

	def __len__(self):
		return len(self.stack)
