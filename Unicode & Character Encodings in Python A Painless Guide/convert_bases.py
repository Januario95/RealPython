from stack import Stack


def convert(n, base):
	conversion = '0123456789ABCDEF'
	if n < base:
		return conversion[n]
	else:
		return convert(n//base, base) + conversion[n%base]


def convert_to_binary(decimal_number):
	stack = Stack()

	while decimal_number > 0:
		remainder = decimal_number % 2
		stack.push(remainder)
		decimal_number = decimal_number // 2

	binary_digits = []
	while not stack.is_empty():
		binary_digits.append(str(stack.pop()))

	return ''.join(binary_digits)

DIGITS = '0123456789abcdef'

def convert_to_base(decimal_number, base):
	stack = Stack()

	while decimal_number > 0:
		remainder = decimal_number % base
		stack.push(remainder)
		decimal_number = decimal_number // base

	new_digits = []
	while not stack.is_empty():
		new_digits.append(DIGITS[stack.pop()])

	return ''.join(new_digits)


num = 20
base = 2
print(convert(num, base))
print(convert_to_binary(num))
print(convert_to_base(num, base))
