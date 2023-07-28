#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 19:20:21

@author: Januario Cipriano
"""

from pathlib import Path
from PyPDF2 import (
    PdfFileReader, PdfFileWriter
)
# filename = 'Emotion and the Art of Negotiation.pdf'

# pdf = PdfFileReader(filename)

# pages = pdf.getNumPages()
# print(pages)
# print(pdf.documentInfo)
# print(pdf.documentInfo.title)

# first_page = pdf.getPage(0)
# print(type(first_page))
# print(first_page.extractText())


# for page in pdf.pages:
#     print(page.extractText())


# out_filename = 'Emotion and the Art of Negotiation.txt'

# with open(out_filename, mode='w', encoding='utf-8') as f:
#     title = pdf.documentInfo.title
#     print(title)
#     num_pages = pdf.getNumPages()
#     f.write(f'{title}\nNumbre of pages: {num_pages}\n')

#     for page in pdf.pages:
#         text = page.extractText()
#         f.write(text)
        
    

pdf_writer = PdfFileWriter()
page = pdf_writer.addBlankPage(width=72,
                               height=72)
print(type(page))





















