#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Feb 14 Tue 2022, 14:05:23

@author: Januario Cipriano
"""

class MyClass:
	pass

c = MyClass()
# print(dir(c))
# o = object()
# print(dir(o))

# raise MyClass

class MyError(Exception):
	pass

# raise MyError


class Employee:
	def __init__(self, id, name):
		self.id = id
		self.name = name

class SalaryEmployee(Employee):
	def __init__(self, id, name, weekly_salary):
		super().__init__(id, name)
		self.weekly_salary = weekly_salary

	def calculate_payroll(self):
		return self.weekly_salary

class HourlyEmployee(Employee):
	def __init__(self, id, name, 
				 hours_worked, hour_rate):
		super().__init__(id, name)
		self.hours_worked = hours_worked
		self.hour_rate = hour_rate

	def calculate_payroll(self):
		return self.hours_worked * self.hour_rate

class ComissionEmployee(SalaryEmployee):
	def __init__(self, id, name, weekly_salary,
				 commission):
		super().__init__(id, name, weekly_salary)
		self.commission = commission

	def calculate_payroll(self):
		fixed = super().calculate_payroll()
		return fixed + self.commission

class PayrollSystem:
	def calculate_payroll(self, employees):
		print('Calculating Payroll')
		print('===================')
		for employee in employees:
			print(f'Payroll for: {employee.id} - {employee.name}')
			print(f'- Check amount: {employee.calculate_payroll()}')
			print('')


salary_employee = SalaryEmployee(
	1, 'John Smith', 1500)
hourly_employees = HourlyEmployee(
	2, 'Jane Doe', 40, 15)
commission_employee = ComissionEmployee(
	3, 'Kevin Bacon', 1000, 250)
payroll_system = PayrollSystem()
payroll_system.calculate_payroll([
	salary_employee,
	hourly_employees,
	commission_employee
])



















