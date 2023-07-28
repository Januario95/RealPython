#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue 14 Mon 2022 14:20:34

@author: Januario Cipriano
"""

class WordCountString(str):
	def words(self, separator=None):
		return len(self.split(separator))

sample_text = WordCountString(
	"""Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime
	mollitia, molestiae quas vel sint commodi repudiandae consequuntur
	voluptatum laborum numquam blanditiis harum quisquam eius sed odit
	fugiat iusto fuga praesentium optio, eaque rerum! Provident similique
	accusantium nemo autem. Veritatis obcaecati tenetur iure eius earum
	ut molestias architecto voluptate aliquam nihil, eveniet aliquid
	culpa officia aut! Impedit sit sunt quaerat, odit, tenetur error,
	harum nesciunt ipsum debitis quas aliquid."""
)
# print(sample_text.words())


class UpperPrintString(str):
	def __str__(self):
		return self.upper()

sample_string = UpperPrintString(
	'Hello, Pythonista!')
# print(sample_string)
# print(repr(sample_string))

class LowerString(str):
	def __new__(cls, string):
		instance = super().__new__(cls, string.lower())
		return instance

sample_string = LowerString(
	'Hello Pythonista!')
print(sample_string)
























