# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 07:43:32 2022

@author: Januario Cipriano
"""

import yaml
import logging
import logging.config


# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')


# Log to the console
# logging.basicConfig(level=logging.DEBUG)
# logging.debug('This will be logged')


# logging.basicConfig(filename='app.log', filemode='a',
#                     format='%(name)s - %(levelname)s - %(message)s')
# logging.warning('This will get logged to a file')


# logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
# logging.warning('This is a Warning')


# logging.basicConfig(format='%(asctime)s - %(message)s',
#                     level=logging.INFO)
# logging.info('Admin logged in')


# logging.basicConfig(format='%(asctime)s - %(message)s',
#                     datefmt='%d-%b-%Y %H:%M:%S')
# logging.warning('Admin logged out')


# name = 'Januario'
# logging.error('%s raised an error', name)


# name = 'John'
# logging.error(f'{name} raised an error')


# a = 5
# b = 0
# try:
#     c = a / b
# except Exception as e:
#     logging.error("Exception occurred", exc_info=True)


# a = 5
# b = 0
# try:
#   c = a / b
# except Exception as e:
#   logging.exception("Exception occurred")



# logger = logging.getLogger('example_Logger')
# logger.warning('This is a warning')


# Create a custom logger
# logger = logging.getLogger(__name__)

# # Create handlers
# c_handler = logging.StreamHandler()
# f_handler = logging.FileHandler('file.log')
# c_handler.setLevel(logging.WARNING)
# f_handler.setLevel(logging.ERROR)

# # Create formatters and add it to handlers
# c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
# f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# c_handler.setFormatter(c_format)
# f_handler.setFormatter(f_format)

# # Add handlers to the logger
# logger.addHandler(c_handler)
# logger.addHandler(f_handler)

# logger.warning('This is a warning')
# logger.error('This ia an error')






# logging.config.fileConfig(fname='file.conf',
#                           disable_existing_loggers=False)

# logger = logging.getLogger(__name__)

# logger.debug('This is a debug MESSAGE')






with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)
    

logger = logging.getLogger(__name__)
logger.debug('This is a DEBUG message')





































