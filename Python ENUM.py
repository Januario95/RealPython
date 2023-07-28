#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
Created on Wed Oct 5  19:54:23 2022

@author: Januario Cipriano
"""

import string
import requests
from enum import (
    auto, IntEnum, unique, Enum,
    IntFlag, Flag
)
from http.client import HTTPSConnection

# RED, GREEN, YELLOW = range(3)
# print(RED, GREEN, YELLOW)


# Enumeration members must be constants
class Day(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


# print(list(Day))
# print(Day)
# print(type(Day.MONDAY))
# print(type(Day.TUESDAY))



class Season(Enum):
    WINTER, SPRING, SUMMER, FALL = range(1, 5)
    
# print(Season)


class Grade(Enum):
    A = 90
    B = 80
    C = 70
    D = 60
    F = 0
    
# print(list(Grade))


class Size(Enum):
    S = 'small'
    M = 'medium'
    L = 'large'
    XL = 'extra large'
    
# print(list(Size))


class Subject:
    def __init__(self, subj_name, subj_val):
        self.subj_name = subj_name
        if not isinstance(subj_val, Grade):
            raise TypeError('Grades must be instances of Enum Grade')
        self.subj_val = subj_val
        
    def __str__(self):
        return f'{self.subj_name} - {self.subj_val}'
    
    def __repr__(self):
        return f'<Subject ({self.subj_name}, {self.subj_val})>'


class Student:
    def __init__(self, fname, lname, shirt_size, subjects=[]):
        self.fname = fname
        self.lname = lname
        if not isinstance(shirt_size, Size):
            raise TypeError('Shirt must be an instance of Size Enum')
        self._shirt_size = shirt_size
        
        self._subjects = []
        for subject in subjects:
            self.raise_on_error(subject)
            self._subjects.append(subject)
            
    def add_subject(self, subject):
        self.raise_on_error(subject)
        self._subjects.append(subject)
        
    def raise_on_error(self, subject):
        if not isinstance(subject, Subject):
            raise TypeError('Grades must be instances of Enum Grade')
        if subject.subj_name in [subj.subj_name for subj in self._subjects]:
            raise TypeError(f'Duplicated: {subject.subj_name} already exists. Subjects can only be added once')
        
    @property
    def subjects(self):
        for subject in self._subjects:
            print(f'{subject!r}')
        
    
            
jany = Student('Januario', 'Cipriano', Size.S,
               [Subject('Maths', Grade.B),
                Subject('Physics', Grade.D),
                Subject('Chemistry', Grade.A)])
chemistry1 = Subject('Chemistry', Grade.A)
# chemistry2 = Subject('Chemistry', Grade.B)    
# jany.add_subject(chemistry1)
# jany.add_subject(chemistry1)
# jany.subjects


class SwitchPosition(Enum):
    ON = True
    OFF = False

# print(list(SwitchPosition))



class UserResponse(Enum):
    YES = 1
    NO = 'NO'


# print(list(UserResponse))
# print(UserResponse.NO)



class Empty(Enum):
    pass


# print(list(Empty))



class BaseTextEnum(Enum):
    def as_list(self):
        try:
            return list(self.value)
        except TypeError:
            return [str(self.value)]



class Alphabet(BaseTextEnum):
    LOWERCASE = string.ascii_lowercase
    UPPERCASE = string.ascii_uppercase
    
print(Alphabet.LOWERCASE.as_list())
# print(Alphabet.UPPERCASE.as_list())



HTTPMethod = Enum(
    'HTTPMethod', ['GET', 'POST', 'PUSH',
                   'PATCH', 'DELETE']    
)

# print(list(HTTPMethod))


class HTTPMethod(Enum):
    GET = 1
    POST = 2
    PUSH = 3
    PATCH = 4
    DELETE = 5


# print(list(HTTPMethod))


names = []
# while True:
#     name = input('Member name: ')
#     if name in {'q': 'Q'}:
#         break
#     names.append(name.upper())

# DynamicEnum = Enum("DynamicEnum", names)
# print(list(DynamicEnum))



HTTPStatusCode = Enum(
    value='HTTPStatusCode',
    names=[
        ('OK', 200),
        ('CREATED', 201),
        ('BAD_REQUEST', 400),
        ('NOT_FOUND', 404),
        ('SERVER_ERROR', 500)
    ]    
)
# print(list(HTTPStatusCode))



class Day(Enum):
    MONDAY = auto()
    TUESDAY = auto()
    WEDNESDAY = auto()
    THURSDAY = auto()
    FRIDAY = auto()
    SATURDAY = auto()
    SUNDAY = auto()
    

# print(list(Day))


# print(help(Enum))

class CardinalDirection(Enum):
    def _generate_next_value_(name, start, count, last_values):
        # print(last_values, end=' ')
        return name[0]

    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()
    
# print(list(CardinalDirection))



class OperatingSystem(Enum):
    UBUNTU = 'linux'
    MACOS = 'darwin'
    WINDOWS = 'win'
    DEBIAN = 'linux'
    

# print(list(OperatingSystem))
# print(OperatingSystem.__members__.items())



# @unique
# class OperatingSystem(Enum):
#     UBUNTU = 'linux'
#     MACOS = 'darwin'
#     WINDOWS = 'win'
#     DEBIAN = 'linux'



class CardinalDirection(Enum):
    NORTH = 'N'
    SOUTH = 'S'
    EAST = 'E'
    WEST = 'W'
    
# print(CardinalDirection.NORTH)
# print(CardinalDirection('N'))
# print(CardinalDirection['NORTH'])



class TrafficLight(Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3

# print(TrafficLight.RED.name)
# print(TrafficLight.RED.value)



class Flavor(Enum):
    VANILLA = 1
    CHOCOLATE = 2
    MINT = 3
    
# for flavor in Flavor:
#     print(flavor)

# for flavor in Flavor:
#     print(flavor.name, '->', flavor.value)


# for name in Flavor.__members__:
#     print(name)

# for name in Flavor.__members__.keys():
#     print(name)


# for member in Flavor.__members__.values():
#     print(member)

# for name, member in Flavor.__members__.items():
#     print(name, '->', member)


def handle_traffic_light(light):
    if light is TrafficLight.RED:
        print('You must stop!')
    elif light is TrafficLight.YELLOW:
        print('Light will change to red, be careful!')
    elif light is TrafficLight.GREEN:
        print('You can continue!')

# handle_traffic_light(TrafficLight.RED)
# handle_traffic_light(TrafficLight.YELLOW)
# handle_traffic_light(TrafficLight.GREEN)



# For Python 3.10 or greater
# def handle_semaphore(light):
#     match light:
#         case Semaphore.RED:
#             print("You must stop!")
#         case Semaphore.YELLOW:
#             print("Light will change to red, be careful!")
#         case Semaphore.GREEN:
#             print("You can continue!")



class AtlanticAveTrafficLight(Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3
    PEDESTRIAN_RED = 1
    PEDESTRIAN_GREEN = 3
    

red = AtlanticAveTrafficLight.RED
# print(red is AtlanticAveTrafficLight.RED)
# print(red is not AtlanticAveTrafficLight.RED)

yellow = AtlanticAveTrafficLight.YELLOW
# print(yellow is red)
# print(yellow is not red)


pedestrain_red = AtlanticAveTrafficLight.PEDESTRIAN_RED
# print(red is pedestrain_red)


class EightAveTrafficLight(Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3
    PEDESTRIAN_RED = 1
    PEDESTRIAN_GREEN = 3
    
# print(AtlanticAveTrafficLight.RED is EightAveTrafficLight.RED)
# print(AtlanticAveTrafficLight.YELLOW is EightAveTrafficLight.YELLOW)



red = AtlanticAveTrafficLight.RED
# print(red == AtlanticAveTrafficLight.RED)
# print(red is AtlanticAveTrafficLight.RED)
# print(red != AtlanticAveTrafficLight.RED)

yellow = AtlanticAveTrafficLight.YELLOW
# print(yellow == red)
# print(yellow != red)


pedestrian_red = AtlanticAveTrafficLight.PEDESTRIAN_RED
# print(red == pedestrain_red)
# print(red is pedestrain_red)


# print(TrafficLight.RED == 1)
# print(TrafficLight.YELLOW == 2)
# print(TrafficLight.GREEN == 3)
# print(TrafficLight.GREEN != 3)


class TrafficLight(Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3

# print(TrafficLight.RED is TrafficLight)
# print(TrafficLight.GREEN is not TrafficLight)


class Season(Enum):
    SPRING = 1
    SUMMER = 2
    AUTUMN = 3
    WINTER = 4
    
# sort_enum_by_value = sorted(Season,
#            key=lambda season: season.value)
# print(sort_enum_by_value)
# sort_enum_by_name = sorted(Season,
#            key=lambda season: season.name)
# print(sort_enum_by_name)



# Adding and Tweaking Member Methods
class Mood(Enum):
    FUNKY = 1
    MAD = 2
    HAPPY = 3
    
    def describe_mood(self):
        return self.name, self.value
    
    def __str__(self):
        return f'I feel {self.name}'
    
    @classmethod
    def favorite_mood(cls):
        return cls.HAPPY
    

# print(Mood.HAPPY)
# print(Mood.HAPPY.describe_mood())
# print(Mood.favorite_mood())


from random import randint

def generate_nums(n=8):
    return [randint(1, 9) for _ in range(n)]

class Sort(Enum):
    ASCENDING = 1
    DESCENDING = 2
    
    def __call__(self, values):
        return sorted(values, reverse=self is Sort.DESCENDING)
    

# numbers = [5, 2, 7, 6, 3, 9, 8, 4]
numbers = generate_nums()
# print(Sort.ASCENDING(numbers))
# print(Sort.DESCENDING(numbers))


class Size(int, Enum):
    S = 1
    M = 2
    L = 3
    XL = 4
    

# print(Size.S > Size.M)
# print(Size.S < Size.M)
# print(Size.L >= Size.M)



class MixinA:
    def a(self):
        print(f"MixinA: {self.value}")
        
class MixinB:
    def b(self):
        print(f"MixinB: {self.value}")
        
class ValidEnum(MixinA, MixinB, str, Enum):
    MEMBER = "value"
    

# ValidEnum.MEMBER.a()
# ValidEnum.MEMBER.b()
# print(ValidEnum.MEMBER.upper())




class Size(IntEnum):
    S = 1
    M = 2
    L = 3
    XL = 4
    

# print(Size.S > Size.M)
# print(Size.S < Size.M)
# print(Size.L >= Size.M)
# print(Size.L <= Size.M)
# print(Size.L > 2)
# print(Size.M < 1)



class Size(IntEnum):
    S = 1
    M = 2
    L = 3
    XL = "4"
    
# print(list(Size))


# class Size(IntEnum):
#     S = 1
#     M = 2
#     L = 3
#     XL = "4.o"



class Role(IntFlag):
    OWNER = 8
    POWER_USER = 4
    USER = 2
    SUPERVISOR = 1
    ADMIN = OWNER | POWER_USER | USER | SUPERVISOR
    
    
john_roles = Role.USER | Role.SUPERVISOR
# print(john_roles)
# print(type(john_roles))


# if Role.USER in john_roles:
#     print("John, you're a user")



# print(Role.OWNER is Role.ADMIN)
# print(Role.SUPERVISOR in Role.ADMIN)


# print(Role.ADMIN + 1)
# print(Role.ADMIN - 2)
# print(Role.ADMIN / 3)
# print(Role.ADMIN < 20)



class Role(Flag):
    OWNER = 8
    POWER_USER = 4
    USER = 2
    SUPERVISOR = 1
    ADMIN = OWNER | POWER_USER | USER | SUPERVISOR

john_roles = Role.USER | Role.SUPERVISOR
# print(john_roles)
# print(type(john_roles))


# if Role.USER in john_roles:
#     print("John, you're a user")

# if Role.SUPERVISOR in john_roles:
#     print("John, you're a supervisor")
    
# print(Role.OWNER in Role.ADMIN)
# print(Role.SUPERVISOR in Role.ADMIN)
# print(Role.SUPERVISOR in Role.ADMIN)
# print(Role.ADMIN + 1)



def process_response(code):
    codes = {
        200: 'Success!',
        201: 'Successfully created!',
        400: 'Bad request',
        404: 'Not Found',
        500: 'Internal server error'
    }
    if code in codes:
        print(codes[code])
    else:
        print('Unexpected status')
    
    

url = 'http://localhost:8000/api/collaborator/'
# connection = HTTPSConnection(url)

# res = requests.get(url)
# code = res.status_code
# print(f'code = {code}')
# process_response(code)

# try:
#     connection.request("GET", "/")
#     response = connection.getresponse()
#     code = response.status_code
#     process_response(code)
# finally:
#     connection.close()
    



        





















