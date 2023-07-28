#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 19:20:21

@author: Januario Cipriano
"""

import os
from pathlib import Path
from PyPDF2 import (
    PdfFileReader, PdfFileWriter, PdfFileMerger
)


# pdf_writer = PdfFileWriter()
# page = pdf_writer.addBlankPage(width=72, height=72)
# print(type(page))
# with Path('blank.pdf').open(mode='wb') as out_file:
#     pdf_writer.write(out_file)
    

# input_pdf = PdfFileReader('Emotion and the Art of Negotiation.pdf')
# pdf_writer = PdfFileWriter()
# first_page = input_pdf.getPage(0)
# pdf_writer.addPage(first_page)
# with Path('first_page.pdf').open(mode='wb') as out_file:
#     pdf_writer.write(out_file)


# pdf_writer = PdfFileWriter()
# for n in range(1, 4):
#     page = input_pdf.getPage(n)
#     pdf_writer.addPage(page)

# with Path('page-1-to-4.pdf').open(mode='wb') as out_file:
#     pdf_writer.write(out_file)


# pdf_writer = PdfFileWriter()
# for n in range(0, 10, 2):
#     page = input_pdf.getPage(n)
#     pdf_writer.addPage(page)
    
# with Path('even-pages.pdf').open(mode='wb') as out_file:
#     pdf_writer.write(out_file)



# pdf_writer = PdfFileWriter()
# for n in range(1, 10, 2):
#     page = input_pdf.getPage(n)
#     pdf_writer.addPage(page)
    
# print(pdf_writer.getNumPages())
# with Path('odd-pages.pdf').open(mode='wb') as out_file:
#     pdf_writer.write(out_file)



# pdf_reader = PdfFileReader('Emotion and the Art of Negotiation.pdf')
# pdf_writer = PdfFileWriter()
# pdf_writer.appendPagesFromReader(pdf_reader)
# with Path('Emotion and the Art of Negotiation-Cloned.pdf').open(mode='wb') as out_file:
#     pdf_writer.write(out_file)




# pdf_merger = PdfFileMerger()
# files = ['Think Fast Talk Smart Abrahams En 43973.pdf', 'even-pages.pdf']
# for path in files:
#     pdf_merger.append(path)
    
# pdf_merger.merge(2, 'odd-pages.pdf')
    
# with Path('merged.pdf').open(mode='wb') as out_file:
#     pdf_merger.write(out_file)



# pdf_writer = PdfFileWriter()
# pdf_reader = PdfFileReader('Emotion and the Art of Negotiation.pdf')
# for n in range(pdf_reader.getNumPages()):
#     page = pdf_reader.getPage(n)
#     if n % 2 == 0:
#         page.rotateClockwise(90)
#     pdf_writer.addPage(page)

# with Path('Emotion and the Art of Negotiation-Rotated.pdf').open(mode='wb') as out_file:
#     pdf_writer.write(out_file)



pdf_reader = PdfFileReader('Emotion and the Art of Negotiation.pdf')
page = pdf_reader.getPage(0)
page = page['/Rotate']
print(page)
























