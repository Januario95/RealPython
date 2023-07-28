#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Created on Fri Oct 8 13:54:45 2022

@author: Januario Cipriano
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


people = {3: 'Jim', 2: 'Jack', 4: 'Jane', 1: 'Jill'}
# print(people)
# print(dict(sorted(people.items())))
# print(sorted(people.items(),
#              key=lambda item: item[1]))


numbers = [5, 3, 4, 3, 6, 7, 3, 2, 3, 4, 1]
# print(sorted(numbers))

words = ["aa", "ab", "ac", "ba", "cb", "ca"]
# print(sorted(words))


def select_second_character(word):
    return word[1]

# print(sorted(words,
#              key=select_second_character))


# print(list(reversed([3, 2, 1])))


people = {3: 'Jim', 2: 'Jack', 4: 'Jane', 1: 'Jill'}
# print(sorted(people))
# print(sorted(people.items()))

# view = people.items()
# print(view)
# people[2] = 'Elvis'
# print(view)


def value_getter(item):
    return item[1]

# print(sorted(people.items(),
#              key=value_getter))
# print(sorted(people.items(),
#              key=lambda item: item[1]))




df = pd.read_csv('Things-To-Buy.csv')
# print(df)

df.loc[3, 'item_name'] = 'Mulunga'
df[['category', 'price']].plot(kind='barh', label='Amount')
plt.yticks(range(5), df['item_name'], 
           rotation=0, fontsize=10)

plt.text(df.loc[4, 'price']-3600, 4-0.5,
         df.loc[4, 'price'])

for id_ in range(4):
    plt.text(df.loc[id_, 'price']+500, id_-0.09,
              df.loc[id_, 'price'])

plt.grid(alpha=0.5, which='major', axis='both')
plt.legend()
plt.savefig('Things-To-Buy.png')
plt.show()
print(help(plt.text)





















