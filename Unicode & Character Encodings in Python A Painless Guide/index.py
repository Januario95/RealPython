import string
# import pandas as pd
from math import ceil, log

whitespace = ' \t\n\r\v\f'
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ascii_letters = ascii_lowercase + ascii_uppercase
digits = '0123456789'
hexdigits = digits + 'abcdef' + 'ABCDEF'
octdigits = '01234567'
punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
printable = digits + ascii_letters + punctuation + whitespace

s = "What's wrong with ASCII?!?!?"
# print(s)
# print(s.rstrip(string.punctuation))
# print(s.strip(string.punctuation))
# print(s.strip(string.printable))

# print(s.isprintable())
# for char in string.printable:
# 	print(f'{char!r} is printable? {char.isprintable()}')



def make_bitseq(s: str) -> str:
	if not s.isascii():
		raise ValueError("ASCII only allowed")
	return " ".join(f"{ord(i):08b}" for i in s)

# print(make_bitseq('bits'))
# print(make_bitseq('CAPS'))
# print(make_bitseq('$25.43'))
# print(make_bitseq('~5'))


def n_possible_values(nbits: int) -> int:
	return 2 ** nbits

"""
	given a range of distinct possible values, 
	how can we find the number of bits, n, 
	that is required for the range to be fully 
	represented? What you’re trying to solve for 
	is n in the equation 2**n = x (where you already 
	know x).
"""

def n_bits_required(nvalues: int) -> int:
	return ceil(log(nvalues) / log(2))

# print(n_bits_required(256))
# print(n_bits_required(110))

# print(n_bits_required(128))
# print(n_possible_values(7))


# print(int('11'))
# print(int('11', base=10)) # 10 is already default
# print(int('11', base=2)) # Binary
# print(int('11', base=8)) # Octal
# print(int('11', base=16)) # Hex


"""
	|Type of Literal |	Prefix   |	Example |
	-----------------------------------------
	|   n/a	         |   n/a     | 	  11    |
	| Binary literal |	0b or 0B | 	 0b11   |
	| Octal literal  |  0o or 0O |   0o11   |
	| Hex literal	 |  0x or 0X |   0x11   |
	-----------------------------------------
"""

# print(11)
# print(0b11) # Binary literal
# print(0o11) # Octal literal
# print(0x11) # Hex literal

# columns = ['Decimal', 'Binary',
# 		   'Octal', 'Hex']
# data = []
# for i in range(21):
# 	row = f'{i}\t0b{i}\t0o{i}\t0x{i}'
# 	data.append(row.split('\t'))

# df = pd.DataFrame(data, columns=columns)
# df.to_excel('number_types.xlsx', index=False)


# print('résumé'.encode('utf-8'))
# print('El Niño'.encode('utf-8'))
# print(b'r\xc3\xa9sum\xc3\xa9'.decode('utf-8'))
# print(b'El Ni\xc3\xb1o'.decode('utf-8'))

# print(' '.join(f'{i:08b}' for i in (0xc3, 0xb1)))

# import locale
# print(locale.getpreferredencoding())

# print(all(len(chr(i).encode('ascii')) == 1 for i in range(128)))
# print(chr(74).encode('ascii'))

# ibrow = '🤨'
# print(len(ibrow))
# print(ibrow.encode('utf-8'))
# print(len(ibrow.encode('utf-8')))
# print(list(b'\xf0\x9f\xa4\xa8'))


letters = 'αβγδ'
rawData = letters.encode('utf-8')
# print(rawData)
# print(rawData.decode('utf-8'))
# print(rawData.decode('utf-16'))

# text = '是的'
# rawData = text.encode('utf-8')
# print(rawData)

import pinyin
print(pinyin.get('你好', format="strip", delimiter=" "))

text = '記者 鄭啟源 羅智堅'
# print(text.encode('utf-16'))
# print(text.encode('utf-32'))
# print(len(text.encode('utf-8')))
# print(len(text.encode('utf-16')))
# print(len(text.encode('utf-32')))

"""
	built-ins:
		ascii()
		bin()
		bytes()
		chr()
		hex()
		int()
		oct()
		ord()
		str()
"""

# ascii() gives you an ASCII-only 
# representation of an object, with 
# non-ASCII characters escaped:
# print(ascii('abcdefg'))
# print(ascii('jalepeño'))
# print(ascii((1, 2, 3)))
# print(ascii(0xc0ffee))

# bin() gives you a binary 
# representation of an integer, 
# with the prefix "0b":
# print(bin(0))
# print(bin(400))
# print(bin(0xc0ffee))
# print([bin(i) for i in [1, 2, 3, 4, 8, 16]])


# bytes() coerces the input to bytes, 
# representing raw binary data:
# print(bytes((104, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100)))
# print(bytes(range(97, 123)))
# print(bytes("real 🐍", "utf-8"))
# print(bytes(10))
# print(bytes.fromhex('c0 ff ee'))
# print(bytes.fromhex('72 65 61 6c 70 79 74 68 6f 6e'))

# chr() converts an integer code point 
# to a single Unicode character:
# print(chr(97))
# print(chr(7048))
# print(chr(1114111))
# print(chr(0x10FFFF))
# print(chr(0b01100100))


# hex() gives the hexadecimal 
# representation of an integer, 
# with the prefix "0x":
# print(hex(100))
# print([hex(i) for i in [1, 2, 4, 8, 16]])
# print([hex(i) for i in range(16)])


# int() coerces the input to int, 
# optionally interpreting the input 
# in a given base:
# print(int(11.0))
# print(int('11'))
# print(int('11', base=2))
# print(int('11', base=8))
# print(int('11', base=16))
# print(int(0xc0ffee - 1.0))
# print(int.from_bytes(b'\x0f', 'little'))
# print(int.from_bytes(b'\xc0\xff\xee', 'big'))

# The Python ord() function converts 
# a single Unicode character to its 
# integer code point:
# print(ord('a'))
# print(ord('e'))
# print(ord('ᮈ'))
# print([ord(i) for i in 'hello world'])


# str() coerces the input to str, 
# representing text:
# print(str('str of string'))
# print(str(5))
# print(str([1, 2, 3, 4]))
# print(str(b"\xc2\xbc cup of flour", "utf-8"))


def make_uchr(code: str):
	return chr(int(code.lstrip('U+').zfill(8), 16))

# print(make_uchr('U+10346'))
# print(make_uchr('U+0026'))

# alef = chr(1575) # Or "\u0627"
# alef_hamza = chr(1571) # or "\u0623"

# print(alef, alef_hamza)
# print(alef.encode('unicode-escape'))
# print(alef_hamza.encode('unicode-escape'))


# data = b'\xbc cup of flour'
# print(data.decode('utf-8')) # error
# print(data.decode('latin-1'))


import unicodedata

# print(unicodedata.name('€'))
# print(unicodedata.lookup('EURO SIGN'))

# print(unicodedata.name('$'))
# print(unicodedata.lookup('DOLLAR SIGN'))

# print(dir(unicodedata))
# print(unicodedata.name('@'))
# print(unicodedata.lookup('COMMERCIAL AT'))

# print(unicodedata.name('%'))
# print(unicodedata.lookup('PERCENT SIGN'))

# for index in range(2956, 3200):
# 	print(chr(index), end=', ')

print(u'\u2713')


for i in range(0, 15000):
	# print(f'\t{i}: ', chr(i))
	print(chr(i), end=', ')