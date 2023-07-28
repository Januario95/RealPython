#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 20:13:21

@author: Januario Cipriano
"""

import csv
import pandas as pd


# with open('employee_birthday.txt') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}.')
#             line_count += 1
#         else:
#             print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}')
#             line_count += 1
#     print(f'Processe {line_count} lines.')



# with open('employee_birthday.txt', mode='r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}.')
#             line_count += 1
#         print(f'\t{row["name"]} works in the {row["department"]}, and was born in {row["birthday month"]}.')   
#         line_count += 1
    



# with open('employee_file.csv', mode='w', newline='') as emp_file:
#     employee_writer = csv.writer(emp_file, delimiter=',')
                                  
#     employee_writer.writerow('name,address,date joined'.split(','))
#     employee_writer.writerow(['John Smith', 'Accounting', 'November'])
#     employee_writer.writerow(['Erica Meyres', 'IT', 'March'])
    
    

# with open('employee_file2.csv', mode='w', newline='') as csv_file:
#     fieldnames = ['emp_name', 'dept', 'birth_month']
#     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
#     writer.writeheader()
#     writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
#     writer.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'})
    
    
    

# df = pd.read_csv('hrdata.csv', index_col='Name',
#                  parse_dates=['Hire Date'])
# print(df)
# # print(df.dtypes)
# print(type(df['Hire Date'][0]))



df = pd.read_csv('hrdata.csv', 
                 index_col='Employee',
                 parse_dates=['Hired'],
                 header=0,
                 names=['Employee', 'Hired', 'Salary', 'Sick Days'])
print(df)
# print(df.dtypes)
# print(type(df['Hired'][0]))
df.to_csv('hrdata_modified.csv')





























