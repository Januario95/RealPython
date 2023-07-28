import string



# whitespace = ' \t\n\r\v\f'
# # print(whitespace)
# ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
# ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# ascii_letters = ascii_lowercase + ascii_uppercase
# # print(ascii_letters)
# digits = '0123456789'
# hexdigits = digits + 'abcdef' + 'ABCDEF'
# # print(hexdigits)
# octdigits = '01234567'
# punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
# printable = digits + ascii_letters + punctuation + whitespace
# print(printable)



s = "What's wrong with ASCII?!?!?"
# print(s.rstrip(string.punctuation))

def convert_base(n, base):
	conversion = "0123456789ABCDEF"
	if n < base:
		return conversion[n]
	else:
		return convert_base(n//base, base) + conversion[n%base]

# for num in range(11):
# 	print(convert_base(num, 2))



def make_bitseq(s: str) -> str:
	if not s.isascii():
		raise ValueError('ASCII only allowed')
	return " ".join(f"{ord(i):08b}" for i in s)

print(make_bitseq('bits'))
print(make_bitseq('CAPS'))
print(make_bitseq('$25.43'))

