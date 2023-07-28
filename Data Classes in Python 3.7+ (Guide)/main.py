import os
import sys
import time
import random
import pandas as pd
import translators as ts
from dataclasses import (
	dataclass, make_dataclass,
	field, fields
)
from math import (
	asin, cos, radians, sin, sqrt
)
from typing import Any, List

@dataclass
class DataClassCard:
	rank: str
	suit: str

# queen_of_hearts = DataClassCard('Q', 'Hearts')
# print(queen_of_hearts)
# print(queen_of_hearts.rank)

class RegularCard:
	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit

	def __repr__(self):
		return (f'{self.__class__.__name__}'
				f'(rank={self.rank!r}, suit={self.suit!r})')

	def __eq__(self, other):
		if other.__class__ is not self.__class__:
			return NotImplemented
		return (self.rank, self.suit) == (other.rank, other.suit)

queen_of_hearts = RegularCard('Q', 'Hearts')
# queen_of_hearts2 = RegularCard('Q', 'Hearts')
# print(queen_of_hearts.rank)
# print(queen_of_hearts)
# print(queen_of_hearts == queen_of_hearts2)
# queen_of_hearts_tuple = ('Q', 'Hearts')
# queen_of_hearts_dict = {'Rank':'Q', 'suit': 'Hearts'}
# print(queen_of_hearts_tuple[0])
# print(queen_of_hearts_dict['suit'])


from collections import namedtuple

NamedTupleCard = namedtuple(
	'NamedTupleCard', ['rank', 'suit'])
# print(NamedTupleCard)
# print(NamedTupleCard.rank)
# print(NamedTupleCard.suit)
# queen_of_hearts = NamedTupleCard('Q', 'Hearts')
# print(queen_of_hearts)
# print(queen_of_hearts == NamedTupleCard('Q', 'Hearts'))
# print(queen_of_hearts == ('Q', 'Hearts'))


# Person = namedtuple('Person',
# 	['first_initial', 'last_name'])
# ace_of_spades = NamedTupleCard('A', 'Spades')
# print(ace_of_spades == Person('A', 'Spades'))

# card = NamedTupleCard('7', 'Diamonds')
# card.rank = '9'

import attr

@attr.s
class AttrsCard:
	rank = attr.ib()
	suit = attr.ib()

# at = AttrsCard('Q', 'Hearts')
# print(at)


@dataclass
class Position:
	name: str
	lat: float
	lon: float

	def __repr__(self):
		return f'{self.name} is at {self.lat}{chr(176)}N, {self.lon}{chr(176)}E'

pos = Position('Oslo', 10.8, 59.9)
# print(pos)

Position = make_dataclass(
	cls_name='Position',
	fields=[
		('name', str),
		('lat', float),
		('lon', float)
	],
	namespace={
		'display': lambda self: f'{self.name} is at {self.lat}{chr(176)}N, {self.lon}{chr(176)}E'
	}
)

pos = Position('Oslo', 10.8, 59.9)
# print(pos.display())


@dataclass
class Position:
	name: str
	lon: float = 0.0
	lat: float = 0.0

# print(Position('Null Island'))
# print(Position('Greenwich', lat=51.8))
# print(Position('Vancouver', -123.1, 49.3))


@dataclass
class WithoutExplicitTypes:
	name: Any
	value: Any = 42

# print(Position(3.14, 'pi day', 2018))


@dataclass
class Position:
	name: str
	lon: float = 0.0
	lat: float = 0.0

	def distance_to(self, other):
		r = 6371  # Earth radius in kilometers
		lam_1, lam_2 = radians(self.lon), radians(other.lon)
		phi_1, phi_2 = radians(self.lat), radians(other.lat)
		h = (sin((phi_2 - phi_1) / 2)**2
			 + cos(phi_1) * cos(phi_2) * sin((lam_2 - lam_1) / 2)**2)
		return 2 * r * asin(sqrt(h))

oslo = Position('Oslo', 10.8, 59.9)
vancouver = Position('Vancouver', -123.1, 49.3)
# print(oslo.distance_to(vancouver))
# print(vancouver.distance_to(oslo))


@dataclass
class PlayingCard:
	rank: str
	suit: str

@dataclass
class Deck:
	cards: List[PlayingCard]

queen_of_hearts = PlayingCard('Q', 'Hearts')
ace_of_spades = PlayingCard('A', 'Spades')
two_cards = Deck([queen_of_hearts, ace_of_spades])
# print(two_cards)

RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = '♣ ♢ ♡ ♠'.split()

def make_french_deck():
	return [PlayingCard(r, s) for s in SUITS for r in RANKS]

# for card in make_french_deck():
# 	print(card)

# print(make_french_deck())



@dataclass
class Deck:
    cards: List[PlayingCard] = field(default_factory=make_french_deck)


# deck = Deck()
# print(deck)
# print(Deck())


@dataclass
class Position:
    name: str
    lon: float = field(default=0.0, 
    				   metadata={'unit': 'degrees'})
    lat: float = field(default=0.0, 
    				   metadata={'unit': 'degrees'})

p = Position('Oslo', 10.8, 23.6)
# print(fields(p))

# lat_unit = fields(Position)[2].metadata['unit']
# print(lat_unit)
# lon_unit = fields(Position)[1].metadata['unit']
# print(lon_unit)
# print(Deck())

@dataclass
class PlayingCard:
	rank: str
	suit: str

	def __str__(self):
		return f'{self.suit}{self.rank}'

ace_of_spades = PlayingCard('A', '♠')
# print(ace_of_spades)
# print(Deck())

# print(ord('♡'))
# print(ord('♠'))

# for i in range(0, 15000):
# 	# print(f'\t{i}: ', chr(i))
# 	print(chr(i), end=', ')

# chars = '➀, ➁, ➂, ➃, ➄, ➅, ➆, ➇, ➈, ➉'.split(', ')
# nums = []
# for char in chars:
# 	nums.append(ord(char))

# print(nums)
# print(ord('⭙'))

# for num in nums:
# 	print(chr(num))

@dataclass
class Deck:
	cards: List[PlayingCard] = field(default_factory=make_french_deck)

	def __repr__(self):
		cards = ', '.join(f'{c!s}' for c in self.cards)
		return f'{self.__class__.__name__}({cards})'

# print(Deck())

queen_of_hearts = PlayingCard('Q', chr(9825))
ace_of_spades = PlayingCard('A', chr(9824))
# print(queen_of_hearts)
# print(ace_of_spades)
# ace_of_spades > queen_of_hearts


@dataclass(order=True)
class PlayingCard:
	rank: str
	suit: str

	def __str__(self):
		return f'{self.suit}{self.rank}'

queen_of_hearts = PlayingCard('Q', chr(9825))
ace_of_spades = PlayingCard('A', chr(9824))
# print(ace_of_spades > queen_of_hearts)
# print(('A', '♠') > ('Q', '♡'))


RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = '♣ ♢ ♡ ♠'.split()
card = PlayingCard('Q', '♡')
# print(RANKS.index(card.rank) * len(SUITS) + SUITS.index(card.suit))


@dataclass(order=True)
class PlayingCard:
	sort_index: int = field(init=False, repr=False)
	rank: str
	suit: str

	def __post_init__(self):
		self.sort_index = (RANKS.index(self.rank) * len(SUITS)
						   + SUITS.index(self.suit))

	def __str__(self):
		return f'{self.suit}{self.rank}'

queen_of_hearts = PlayingCard('Q', '♡')
# print(queen_of_hearts.sort_index)
ace_of_spades =  PlayingCard('A', '♠')
# print(ace_of_spades.sort_index)
# print(ace_of_spades > queen_of_hearts)


from random import sample

# print(Deck(sample(make_french_deck(), k=10)))


@dataclass
class Position:
	name: str
	lon: float = 0.0
	lat: float = 0.0

# pos = Position('Oslo', 10.8, 59.9)
# print(pos.name)
# pos.name = 'Stockholm'


@dataclass(frozen=True)
class ImmutableCard:
	rank: str
	suit: str

@dataclass(frozen=True)
class ImmutableDeck:
	cards: List[ImmutableCard]

# queen_of_hearts = ImmutableCard('Q', '♡')
# ace_of_spades = ImmutableCard('A', '♠')
# deck = ImmutableDeck([queen_of_hearts, ace_of_spades])
# print(deck)
# deck.cards[0] = ImmutableCard('7', '♢')
# print(deck)



# @dataclass
# class Position:
# 	name: str
# 	lon: float
# 	lat: float

# @dataclass
# class Capital(Position):
# 	country: str

# print(Capital('Oslo', 10.8, 59.9, 'Norway'))


@dataclass
class Position:
	name: str
	lon: float = 0.0
	lat: float = 0.0

@dataclass
class Capital(Position):
	country: str = 'Unknown'
	lat: float = 40.0

# print(Capital('Madrid', country='Spain'))


@dataclass
class SimplePosition:
	name: str
	lon: float
	lat: float

@dataclass
class SlotPosition:
	__slots__ = ['name', 'lon', 'lat']
	name: str
	lon: float
	lat: float

from pympler import asizeof

simple = SimplePosition('London', -0.1, 51.5)
slot = SlotPosition('Madrid', -3.7, 40.4)
# print(asizeof.asizeof(simple, slot))

from timeit import timeit

# print(timeit('slot.name', setup="slot=SlotPosition('Oslo', 10.8, 59.9)", globals=globals()))
# print(timeit('simple.name', setup="simple=SimplePosition('Oslo', 10.9, 59.9)", globals=globals()))



# print(ord('♡'))
# print(ord('♠'))

for i in range(0, 15000):
	# print(f'\t{i}: ', chr(i))
	print(chr(i), end=', ')

# chars = '①, ②, ③, ④, ⑤, ⑥, ⑦, ⑧, ⑨, ⑩, ⑪, ⑫, ⑬, ⑭, ⑮, ⑯, ⑰, ⑱, ⑲, ⑳'.split(', ')
# nums = []
# for char in chars:
# 	nums.append(ord(char))

# print(nums)
# print(ord('⭙'))
# print(ord('✓'))
# print(ord('✗'))
# print(ord('✔'))
# print(ord('✘'))
# print(ord('Ⓐ'))
# print(ord('Ⓡ'))
# print(ord('Ǣ'))
# print(ord('Ȓ'))
print(ord('᚛'))
print(ord('᚜'))
print(ord('⇚'))
print(ord('⇛'))
print(ord('⋘'))
print(ord('⋙'))
print(ord('ᐳ'))
print(ord('ᐸ'))

# print(chr(10003))
# print(chr(10007))
# print(chr(10004))
# print(chr(10008))

# for num in nums:
# 	print(num, ':', chr(num))


def display_text_std(text):
	try:
		delay = 1/len(text)+0.01
	except Exception as e:
		delay = 0.02
	sys.stdout.write('\t')
	for char in text:
		sys.stdout.write(f'{char}')
		sys.stdout.flush()
		time.sleep(delay)

	print('')

# with open('data2.txt', mode='r') as f:
# 	data = f.read()

from_language = 'en'
langs = ['pt', 'fr', 'lt']
to_language = 'pt'
# query_text = data.get('query_text')


unique = []
all_words = []
# for line in data.split('\n'):
# 	for word in line.split(' '):
# 		# all_words.append(word)
# 		if word not in unique:
# 			unique.append(word)

	# try:
	# 	display_text_std(line)
	# 	lang = random.choice(langs)
	# 	display_text_std(f'Translating to {lang}')
	# 	translation = ts.translate_text(
	# 	    query_text=line,
	# 	    from_language=from_language,
	# 	    to_language=lang)
	# 	display_text_std(translation)
	# except Exception as e:
	# 	pass

words = []
# for word in unique:
# 	row = {}
# 	try:
# 		row['English'] = word
# 		translation = ts.translate_text(
# 		    query_text=word,
# 		    from_language=from_language,
# 		    to_language='pt')
# 		row['Portuguese'] = translation
# 		words.append(row)
# 		print(row)
# 	except Exception as e:
# 		print(e)

# print(len(all_words))
# print(len(unique))

# print(words)

# words = [
# 	{'English': 'Income', 'Portuguese': 'Rendimento'}, 
# 	{'English': 'refers', 'Portuguese': 'Se refere'}, 
# 	{'English': 'to', 'Portuguese': 'Para'}, 
# 	{'English': 'the', 'Portuguese': 'o'}, 
# 	{'English': 'money', 'Portuguese': 'dinheiro'}, 
# 	{'English': 'that', 'Portuguese': 'Isso'}, 
# 	{'English': 'a', 'Portuguese': 'um'}, 
# 	{'English': 'person', 'Portuguese': 'pessoa'}, 
# 	{'English': 'or', 'Portuguese': 'ou'}, 
# 	{'English': 'entity', 'Portuguese': 'entidade'}
# ]
# df = pd.DataFrame(words)
# df = pd.read_excel('English-Portuguese.xlsx')
# df.sort_values(by=['English'], inplace=True)
# df.to_excel('English-Portuguese.xlsx', index=False)
# os.system('start English-Portuguese.xlsx')