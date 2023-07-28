#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Created on Fri Oct 8 14:09:13 2022

@author: Januario Cipriano
"""

import math
import time
import random
import requests
import functools
from datetime import datetime


def add_one(number):
    return number + 1

# print(add_one(2))


def say_hello(name):
    return f"Hello {name}"

def be_awesome(name):
    return f"You {name}, together we are the awesomest!"

def greet_bob(greeter_func):
    return greeter_func("Bob")

# print(greet_bob(say_hello))
# print(greet_bob(be_awesome))


def parent():
    print("Printing from the parent() function")
    
    def first_child():
        print("Priting from the first_child() function")
        
    def second_child():
        print("Priting from the second_child() function")
        
    second_child()
    first_child()
    
# parent()



def parent(num):
    def first_child():
        return "Hi, I am Emma"
    
    def second_child():
        return "Call me Liam"
    
    if num == 1:
        return first_child
    else:
        return second_child
    
# first = parent(1)
# second = parent(2)

# print(first())
# print(second())



def my_decorator(func):
    def wrapper():
        print("Something is happening before the function called")
        func()
        print("Something is happening after the function is called")
    return wrapper

def say_whee():
    print("Whee!")
    
# say_whee = my_decorator(say_whee)
# print(say_whee())



def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass
        
    return wrapper

def say_whe():
    print("Whee!")
    
# say_whee = not_during_the_night(say_whee)
# say_whee()



def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called")
        func()
        print("Something is happening after the function is called")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")


# So, @my_decorator is just an easier way of saying
# say_whee = my_decorator(say_whee).

# say_whee()


def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice

@do_twice
def say_whee():
    print("Whee!")

# say_whee()


def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def greet(name):
    print(f"Hello, {name}")

# greet('World')

@do_twice
def return_greeting(name):
    print("Creating greeitng")
    return f"Hi {name}"


# hi_adam = return_greeting('Adam')
# print(hi_adam)


def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"

# print(return_greeting('Adam'))



# print(print)
# print(print.__name__)
# print(help(print))


# print(say_whee)
# print(say_whee.__name__)
# print(help(say_whe))



def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def say_whee(name):
    return f"Hi {name}"

# print(say_whee)
# print(say_whee.__name__)
# print(help(say_whee))


def timer(func):
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f'Finished {func.__name__!r} in {run_time:.4f} seconds')
        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

# waste_some_time(999)
    



def debug(func):
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")
        return value
    return wrapper_debug

@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you are growing up"

# print(make_greeting('Janu'))
# print(make_greeting('Richard', age=112))



math.factorial = debug(math.factorial)

def approximate_e(terms=18):
    return sum(1 / math.factorial(n) for n in range(terms))

# print(approximate_e())


def slow_down(func):
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down

@slow_down
def countdown(from_number):
    if from_number < 1:
        print('Liftoff!')
    else:
        print(from_number)
        countdown(from_number - 1)

# countdown(5)


class LimitQuery:
    def __init__(self, func):
        self.func = func
        self.count = 0
        
    def __call__(self, *args, **kwargs):
        limit = args[0]
        if self.count < limit:
            self.func()
            self.count += 1
        else:
            print('No query left!')

@LimitQuery    
def fetch_api():
    res = requests.get('http://localhost:8000/api/collaborators/')
    print(res.status_code)
    # print(res.json())
    
# fetch_api(4)
# fetch_api(4)
# fetch_api(4)
# fetch_api(4)
# fetch_api(4)



PLUGINS = dict()


def register(func):
    """Register a function as a plug-in"""
    PLUGINS[func.__name__] = func
    return func

@register
def say_hello(name):
    return f"Hello {name}"

@register
def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def randomly_greet(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(f"Using {greeter!r}")
    return greeter_func(name)


# randomly_greet('Jaci')
# print(PLUGINS)



class TimeWaster:
    @debug
    def __init__(self, max_num):
        self.max_num = max_num
        
    @timer
    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(self.max_num)])

# tw = TimeWaster(1000)
# tw.waste_time(9999)



@timer
class TimeWaster:
    def __init__(self, max_num):
        self.max_num = max_num
        
    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(self.max_num)])
            
# tw = TimeWaster(1000)
# tw.waste_time(99998)         
            
            



class Counter:
    def __init__(self, start=0):
        self.count = start
    
    def __call__(self):
        self.count += 1
        if self.count > 3:
            raise ValueError('You can only call the instance three times!')
        print(f'Current count is {self.count}')
        
counter = Counter()
counter()
counter()
counter()
counter()





































