import time
from random import randint, choice
from selenium import webdriver
from selenium.webdriver.common.by import By

class Fraction:
	def __init__(self, nume, deno):
		self.nume = nume
		self.deno = deno

	def __str__(self):
		return f'{self.nume}/{self.deno}'

	def __add__(self, other_func):	
		new_nume = self.nume * other_func.deno + other_func.nume * self.deno
		new_demo = self.deno * other_func.deno
		return Fraction(new_nume, new_demo)

	def __mul__(self, other_func):
		new_nume = self.nume * other_func.nume
		new_demo = self.deno * other_func.deno
		return Fraction(new_nume, new_demo)

	def __sub__(self, other_func):
		new_nume = self.nume * other_func.deno - other_func.nume * self.deno
		new_demo = self.deno * other_func.deno
		return Fraction(new_nume, new_demo)

	def __truediv__(self, other_func):
		other_func = Fraction(other_func.deno, other_func.nume)
		return self.__mul__(other_func)

# fr1 = Fraction(2, 3)
# fr2 = Fraction(3, 4)
# print(fr1 + fr2)
# print(fr1 * fr2)
# print(fr1 - fr2)
# print(fr1 / fr2)
# print(fr1 + fr2)


options = webdriver.ChromeOptions()
options.add_argument('--incognito')

driver = webdriver.Chrome('C:/Users/a248433/Documents/drivers/chromedriver106.exe',
                options=options)
driver.maximize_window()

driver.get('http://localhost:8000/fraction_calculator/')
time.sleep(2)

def get_element(class_name):
	return driver.find_element(By.CLASS_NAME, class_name)

nume1 = get_element('nume1')
nume2 = get_element('nume2')
deno1 = get_element('deno1')
deno2 = get_element('deno2')
operator = get_element('operator')
SYMBOLS = ['+', '-', ':', 'x']

def clear_values():
	nume1.clear()
	deno1.clear()
	nume2.clear()
	deno2.clear()
	time.sleep(0.5)

def ser_values(tag):
	tag.send_keys(randint(1, 10))
	time.sleep(0.5)

button = driver.find_element(By.CLASS_NAME, 'calculate')
for i in range(10):
	clear_values()

	ser_values(nume1)
	ser_values(deno1)

	operator.send_keys(choice(SYMBOLS))
	time.sleep(0.5)

	ser_values(nume2)
	ser_values(deno2)

	button.click()
	time.sleep(1)









